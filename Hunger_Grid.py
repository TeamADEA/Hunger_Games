import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
# GRASS = 0
# LAVA = 1
# BERRIES = 2
# KATS = 3
# WALLS  = 4

LAVA_CHANCE = .02
BERRY_CHANCE = .05

def createHungerGrid(M = 34, N = 34, STATIC=True):
    """
    Create a grid of MxN size (default 34x34), 2 thick 'Wall' on the outsdie.
    Randomly place lava and berries based on the global LAVA/BERRY_CHANCE. STATIC
    determines how random numbers are generated, if TRUE, seed is 123456. Else
    make new seed each time.
    """
    tempGrid = np.zeros(shape=(M,N))
    if(STATIC):
        np.random.seed(123456)
    randLavaGrid = np.random.rand(M,N)
    np.place(tempGrid, randLavaGrid < LAVA_CHANCE, 1)
    randBerryGrid = np.random.rand(M,N)
    np.place(tempGrid, randBerryGrid < BERRY_CHANCE, 2)
    
    tempGrid[0:2, :] = 4    # Top Row
    tempGrid[-2:, :] = 4    # Bottom Row
    tempGrid[:, 0:2] = 4    # Left Side
    tempGrid[:, -2:] = 4    # Right Side
    
    return tempGrid

hungerGrid = createHungerGrid()
hungerGrid[4,10] = 3

################################################################################
plt.ion()
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes((0,0,1,1))

LAVA_COLOR    = '#FF6600'
GRASS_COLOR   = '#00FF00'
BERRY_COLOR   = '#0000FF'
KATS_KOLOR    = '#EEFF11'
WALL_COLOR    = '#696969'
hunger_color = col.ListedColormap([GRASS_COLOR, LAVA_COLOR, BERRY_COLOR, KATS_KOLOR, WALL_COLOR])
img = ax.imshow(hungerGrid, cmap= hunger_color, interpolation='none')
plt.pause(.1)