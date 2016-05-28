import matplotlib.pyplot as plt
import matplotlib.colors as col
import numpy as np
from hg_settings import *
LAVA_COLOR    = '#FF6600'
GRASS_COLOR   = '#A5D414'
BERRY_COLOR   = '#7722FF'
KATS_KOLOR    = '#552222'
WALL_COLOR    = '#898989'
HUNGER_COLOR = col.ListedColormap([GRASS_COLOR, LAVA_COLOR, BERRY_COLOR, KATS_KOLOR, WALL_COLOR])

class Visualizer(object):
    """Visualize the simulation.

    Attributes
    ----------
    grid : 2D numpy array
        The environment that Kat agent lives in.
    """
    def __init__(self, grid):
        self.fig = plt.figure(figsize=(12,6))
        self.ax = self.fig.add_axes((-.25,0,1,1))
        self.info = self.fig.add_axes((0,0,1,1))
        self.img = self.ax.imshow(grid.get_grid(), cmap= HUNGER_COLOR, interpolation='none')
        self.ax.axis('off')
        self.info.axis('off')

    def show(self, grid, kats, gen):
        self.img.set_data(grid[0])
        genNum = str("Generation " + str(gen))
        generation = self.info.text(.5,.95,genNum, fontsize = 18 )
        ins = str("CURRENT INSTRUCTION SET: " + grid[1])
        """
        if (type(kats)==list):
            for i in range(len(kats)):
               ins += str("PREVIOUS " +str(i) + " INSTRUCTION SET: " + kats[i].print_ins_1() + "\n")
        else:
            ins += str("PREVIOUS INSTRUCTION SET: " + kats.print_ins_1())
        """
        ins_set = self.info.text(.5,.8,ins,  verticalalignment='top',
                    horizontalalignment='left', fontsize = 12)
        plt.draw()
        plt.pause(.01)
        generation.remove()
        ins_set.remove()

    def graph(self, array):
        plt.figure()
        for i in range(SEPERATE_MODELS): 
            plt.plot(array[i])
        plt.title('Fitness over Generations')
        plt.xlabel('Number of generations')
        plt.ylabel('Fitness')
        plt.ylim(0, (np.max(array) + 10))
        plt.show()
        
    def ins_graph(self, array):
        plt.figure(1)
        
        plt.subplot(211)
        title = str('AVG: # Of Instructions VS % Of Instruction Types FOR [' + \
                str(NUM_SIMS) + '] GENERATIONS')
        plt.title(title)
        plt.ylabel('# Of Instructions')
        plt.ylim(0, np.max(array[:,5])+1)
        plt.plot(array[:,5])
        
        plt.subplot(212)
        plt.xlabel('Number of generations')
        plt.ylabel('% Of Instrucitions')
        plt.plot(array[:,0], color=GRASS_COLOR)
        plt.plot(array[:,1], color=LAVA_COLOR )
        plt.plot(array[:,2], color=BERRY_COLOR)
        plt.plot(array[:,3], color=KATS_KOLOR)
        plt.plot(array[:,3], color=WALL_COLOR)
        plt.show()
