import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import Hunger_Grid as hg
import Kat

class simManager():
    grid = None
    
    
    def __init__(self):
        self.grid = hg.createHungerGrid()

    def visualize(self,hungerGrid, katArray):
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