import copy
import numpy as np
import Hunger_Grid as hg
#import Mutate as m
from Kat import Kat
from Visualize import Visualizer
from hg_settings import *

GRID_DIMENSION = 34
NUM_KATS = 20

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
    def __init__(self, seedKat):
        self.grid = hg.createHungerGrid(GRID_DIMENSION,GRID_DIMENSION)
        self.kats = [Kat(0,0) for i in range(NUM_KATS)]
	self.playback = []
				
        for i in range(NUM_KATS):
            if(i <= AMT_MUTATE):
               self.kats[i] = seedKat.clone()
            """
            else:
                kats.append(m.mutate_kat(seedKat.clone()))
            """
        for k in self.kats:
            self.setKatPosition(k)
    
    def update(self):
        for k in self.kats:
            if(k.dead == False):
                direction = MOVE[k.make_decision(self.grid)]
                nextX = k.xLoc + direction[1]
                nextY = k.yLoc + direction[0]
                self.grid[k.yLoc, k.xLoc] = GRASS
                
                
                if(self.grid[nextY,nextX] == LAVA):
                    k.dead = True
                
                elif(self.grid[nextY, nextX] == BERRY):
                    k.eat_berry()
                    k.take_step(nextY, nextX)
                    self.grid[k.yLoc, k.xLoc] = KAT
                
                elif(self.grid[nextY, nextX] == GRASS):
                    k.take_step(nextY, nextX)
                    self.grid[k.yLoc, k.xLoc] = KAT
        
        self.playback.append(self.grid)
                            
    def setKatPosition(self, kat):
        randX = np.random.randint(2, GRID_DIMENSION - 3)
        randY = np.random.randint(2, GRID_DIMENSION - 3)
        
        if(self.grid[randY,randX] == GRASS):
            kat.xLoc = randX
            kat.yLoc = randY
            self.grid[randY, randX] = 3
            return
        else:
            self.setKatPosition(kat)

    def return_playback(self):
        return self.playback
        
    def top_kat(self):
        top_score = self.kats[0].calculate_fitness()
        top_location = 0
        for i in range(NUM_KATS):
            if(self.kats[i].calculate_fitness() > top_score):
                top_score = self.kats[i].calculate_fitness()
                top_location = i    
        return self.kats[top_location].clone(), top_score
        