import matplotlib.pyplot as plt
import matplotlib.colors as col

LAVA_COLOR    = '#FF6600'
GRASS_COLOR   = '#A5D414'
BERRY_COLOR   = '#7722FF'
KATS_KOLOR    = '#552222'
WALL_COLOR    = '#898989'
HUNGER_COLOR = col.ListedColormap([GRASS_COLOR, LAVA_COLOR, BERRY_COLOR, KATS_KOLOR, WALL_COLOR])

class Visualizer():
    """Visualize the simulation.
	
    Attributes
    ----------
    grid : 2D numpy array
        The environment that Kat agent lives in.
    """
    def __init__(self, grid):
	self.fig = plt.figure(figsize=(6,6))
	self.ax = self.fig.add_axes((0,0,1,1))
        self.img = self.ax.imshow(grid, cmap= HUNGER_COLOR, interpolation='none')
        

    def show(self, grid):
        self.img.set_data(grid)
        plt.draw()
        plt.pause(.01)
    
    def graph(self, array):
        #plt.figure(figsize=(6,6))
        #plt.axes([.1,.1,1,.8])
        plt.figure()
        plt.plot(array)
        plt.title('Fitness over Generations')
        plt.xlabel('Number of generations')
        plt.ylabel('Fitness')
        plt.show()
        