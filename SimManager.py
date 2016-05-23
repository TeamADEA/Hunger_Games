import copy
import numpy as np
import Hunger_Grid as hg
import Mutate as m
from Kat import Kat
from Visualize import Visualizer
from hg_settings import *


GRID_DIMENSION = 34
NUM_KATS = NUM_OF_TRIALS

# MOVE = {[-1,0]:"UP", [0,1]:"RIGHT", [1,0]:"DOWN", [0,-1]:"LEFT"}
MOVE = [[-1,0],[0,1],[1,0],[0,-1]]

class sim_manager():
    """
    Attributes
    ----------
    seedKat : Kat
        The first Kat agent.

    Other Attributes
    ----------------
    grid : 2D numpy array
        The environment that Kats agents will live in, with the states
        of each cell already set.

    kats : list
        A list of Kats agent

    vis : Visualizer
	    A Visualizer class used to visualize simulation, observe
        simulation, and diagnose possible problem.
    """
    def __init__(self, seedKat, hunger_grid, multi_cat=False):
        self.grid = np.array(hunger_grid.get_grid())

        if not multi_cat:
            self.kats = [seedKat.clone() for i in range(NUM_KATS)]
        else:
            temp_kats = seedKat * (NUM_OF_TRIALS/5)
            self.kats = []
            for kat in temp_kats:
                self.kats.append(kat.clone())
        self.playback = []

        # Print Statements
        #seedKat.print_ins_1()
        #seedKat.print_ins_2()

        for i in range(NUM_KATS):
            #self.kats[i] = seedKat.clone()
            if(i >= AMT_CLONE):
                m.mutate_kat(self.kats[i])

        for k in self.kats:
            self.setKatPosition(k)

    def update(self, kat_num):
        """Update the Kat agents at each time step.

        Only update Kat agents that are alive. First ask
		Kat agent where they want to move, then record the
		next move's x and y location. According to different
		state of the next cell, different action will be taken.
        """
        if(self.kats[kat_num].dead == False):
            direction = MOVE[self.kats[kat_num].make_decision(self.grid)]
            nextX = self.kats[kat_num].xLoc + direction[1]
            nextY = self.kats[kat_num].yLoc + direction[0]
            self.grid[self.kats[kat_num].yLoc, self.kats[kat_num].xLoc] = GRASS


            if(self.grid[nextY,nextX] == LAVA):
                self.kats[kat_num].die()

            elif(self.grid[nextY, nextX] == BERRY):
                self.kats[kat_num].eat_berry()
                self.kats[kat_num].take_step(nextY, nextX)
                self.grid[self.kats[kat_num].yLoc, self.kats[kat_num].xLoc] = KAT

            elif(self.grid[nextY, nextX] == GRASS):
                self.kats[kat_num].take_step(nextY, nextX)
                self.grid[self.kats[kat_num].yLoc, self.kats[kat_num].xLoc] = KAT
        self.playback.append(copy.deepcopy(self.grid))

    def setKatPosition(self, kat):
        """Set the Kat agent's initial position.

        A Kat agent object is passed in, a random cell is
		selected (inside the wall), and until it finds
		a cell with GRASS as the state, it will continue
		call itself recursively.
        """
        kat.xLoc = GRID_DIMENSION/2
        kat.yLoc = GRID_DIMENSION/2
        """
        randX = np.random.randint(2, GRID_DIMENSION - 3)
        randY = np.random.randint(2, GRID_DIMENSION - 3)

        if(self.grid[randY,randX] == GRASS):
            kat.xLoc = randX
            kat.yLoc = randY
            self.grid[randY, randX] = 3
            return
        else:
            self.setKatPosition(kat)
        """

    def return_playback(self):
        return self.playback

    def top_kat(self):
        """Find the top fitness score of all Kat agents.

        First it takes the fitness score of first Kat in
		the list. As it loops through the list, when a higher
		fitness score found, top_score is updated, the Kat with
		the highest fitness score is cloned and returned along
		with the fitness score.
        """
        top_score = 0
        top_location = 0
        print "Kat Fitness: "
        for i in range(NUM_KATS):
            print self.kats[i].calculate_fitness()
            if(self.kats[i].calculate_fitness() > top_score):
                top_score = self.kats[i].calculate_fitness()
                top_location = i
        print "Winning Score: ", top_score
        print "TOP KAT INS1: "
        self.kats[top_location].print_ins_1()
        return copy.deepcopy(self.kats[top_location].clone()), top_score

    def top_kats(self):
        def get_key(kat):
            return kat.calculate_fitness()
        top_kats = sorted(self.kats, key=get_key)
        return top_kats[-5:]

    def average_fitness(self):
        total_fitness = sum([i.calculate_fitness() for i in self.kats])
        return total_fitness / float(len(self.kats))

    def clear_grid(self, hunger_grid):
        self.grid = np.array(hunger_grid.get_grid())
