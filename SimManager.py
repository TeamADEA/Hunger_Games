import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import Hunger_Grid as hg
from Kat import Kat
from hg_settings import *

GRID_DIMENSION = 34
NUM_KATS = 20

# MOVE = {[-1,0]:"UP", [0,1]:"RIGHT", [1,0]:"DOWN", [0,-1]:"LEFT"}
MOVE = [[-1,0],[0,1],[1,0],[0,-1]]
class simManager():
    grid = None
    kats = []
    
    def __init__(self, seedKat):
        self.grid = hg.createHungerGrid(GRID_DIMENSION,GRID_DIMENSION)
        self.kats.append(seedKat)
        for i in range(1, NUM_KATS):
            if(i <= 20):
               self. kats.append(seedKat.clone())
            """
            else:
                kats.append(mutateKat(seedKat.clone()))
            """
        for k in self.kats:
            self.setKatPosition(k)
    def update(self):
        for k in self.kats:
            direction = MOVE[k.make_decision(self.grid)]
            nextX = k.xLoc + direction[1]
            nextY = k.yLoc + direction[0]
            self.grid[kat.yLoc,kat.xLoc] = GRASS
            k.take_step(nextY, nextX)
            
            if(self.grid[k.yLoc,k.xLoc] == LAVA):
                k.dead = True
            elif(self.grid[k.yLoc,k.xLoc] == BERRY):
                k.eat_berry()
                self.grid[k.yLoc, k.xLoc] = KAT
            elif(self.grid[k.yLoc,k.xLoc] == GRASS):
                self.grid[k.yLoc, k.xLoc] = KAT
                
    def setKatPosition(self, kat):
        randX = np.random.randint(2, GRID_DIMENSION - 2)
        randY = np.random.randint(2, GRID_DIMENSION - 2)
        
        if(self.grid[randY,randX] == GRASS):
            kat.xLoc = randX
            kat.yLoc = randY
            self.grid[randY, randX] = 3
            return
        else:
            self.setKatPosition(kat)

    def visualize(self):
        ################################################################################
        plt.ion()
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_axes((0,0,1,1))
        
        LAVA_COLOR    = '#FF6600'
        GRASS_COLOR   = '#A5D414'
        BERRY_COLOR   = '#7722FF'
        KATS_KOLOR    = '#552222'
        WALL_COLOR    = '#898989'
        hunger_color = col.ListedColormap([GRASS_COLOR, LAVA_COLOR, BERRY_COLOR, KATS_KOLOR, WALL_COLOR])
        img = ax.imshow(self.grid, cmap= hunger_color, interpolation='none')
        plt.pause(.1) 
        
kat = Kat(0,0)
test = simManager(kat)
test.update()
test.visualize()