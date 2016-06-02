"""
The variables below can be changed to manipulate the simulations
"""
#number of kats in each generation
#Should be divisible by 5
#as the top 5 kats will be used to seed the next generation
NUM_OF_INDIVIDUALS = 25 # Should be divisible by 5

# NUMBER OF GENERATIONS
#NUM_SIMS = 10 # OLD NAMING SCHEME
NUM_OF_GENERATIONS = 100

#HOW MANY TIMES THE MODEL WILL RUN IN A ROW
#SEPERATE_MODELS = 1 #OLD NAMING SCHEME
NUM_OF_SPECIES = 10

# MAXIMUM STEPS PER SIMULATION
STEPS_PER_SIM =300

#FITNESS VALUES
STEP_VALUE = 1
BERRY_VALUE = 100

# FIXED MAP FEATURES
WALLS_OF_DEATH  = False  # Walls are lava
WALL_PILLARS    = False  # Wall tiles periodically jut out

"""
Variables below this point should not be changed as they are integral to the 
functioning of the program
"""

# DISPLAY THE GRAPHS OR NOT
DISPLAY_GRAPHS = True

# NUMBER OF PURE CLONES WITHIN A GENERATION
#having this be 5 will ensure that each of the 5 seed kats is cloned without mutation
AMT_CLONE = 5

# MOVE CODES
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DO_NOTHING = 4
MOVE_STRING = ["MOVE [UP]","MOVE [RIGHT]","MOVE [DOWN]","MOVE [LEFT]","[DON'T] MOVE`"]

# TILES CODES
GRASS = 0
LAVA = 1
BERRY = 2
KAT = 3
WALL  = 4
TILE_STRING = ["[GRASS]","[LAVA]","[BERRY]","[KAT]","[WALL]"]

# KAT'S VISION RANGE
VISION_RANGE = 1


