import matplotlib.pyplot as plt
import matplotlib.colors as col

LAVA_COLOR    = '#FF6600'
GRASS_COLOR   = '#A5D414'
BERRY_COLOR   = '#7722FF'
KATS_KOLOR    = '#552222'
WALL_COLOR    = '#898989'
HUNGER_COLOR = col.ListedColormap([GRASS_COLOR, LAVA_COLOR, BERRY_COLOR, KATS_KOLOR, WALL_COLOR])

class Visualizer():
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_axes((0,0,1,1))
    img = ax
    
    def __init__(self, grid):
        self.img = self.ax.imshow(grid, cmap= HUNGER_COLOR, interpolation='none')
    
    def show(self, grid):
        self.img.set_data(grid)
        plt.show()
        plt.pause(.01) 