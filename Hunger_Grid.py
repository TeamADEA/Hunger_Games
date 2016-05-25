import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.colors as col
from hg_settings import *
# GRASS = 0
# LAVA = 1
# BERRIES = 2
# KATS = 3
# WALLS  = 4

LAVA_CHANCE = .02
BERRY_CHANCE = .05


class hunger_grid():

    def __init__(self):
        self.hung_grid = self.createHungerGrid()
        

    def createHungerGrid(self, M = 34, N = 34, seed = 123, P_LAVA = .02, P_BERRY = .05):
        """Create a grid of MxN size (default 34x34), 2 thick 'Wall' on the outside.
        Randomly place lava and berries based on the global LAVA/BERRY_CHANCE. STATIC
        determines how random numbers are generated, if TRUE, seed is 123456. Else
        make new seed each time.
        """
        np.random.seed(seed)
        tempGrid = np.zeros(shape=(M,N))

        randLavaGrid = np.random.rand(M,N)
        np.place(tempGrid, randLavaGrid < P_LAVA, LAVA)
        randBerryGrid = np.random.rand(M,N)
        np.place(tempGrid, randBerryGrid < P_BERRY, BERRY)

        if WALL_PILLARS:
            tempGrid[2,3:-2:5] = WALL
            tempGrid[-3,5:-2:5] = WALL
        # Intentional placements (tests)
        # tempGrid[2,2:-2] = LAVA
        # tempGrid[-3,2:-2] = LAVA
        # tempGrid[16,17] = LAVA
        # tempGrid[17,18] = LAVA
        # tempGrid[18,17] = LAVA
        # tempGrid[2,6] = LAVA

        # Walls
        border = WALL
        tempGrid[0:2, :] = border  # Top Row
        tempGrid[-2:, :] = border  # Bottom Row
        tempGrid[:, 0:2] = border  # Left Side
        tempGrid[:, -2:] = border  # Right Side


        hung_grid = np.array(tempGrid, dtype=int)
        return hung_grid

    def get_grid(self):
        return copy.deepcopy(self.hung_grid)
