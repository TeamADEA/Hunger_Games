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

#FITNESS VALUES
STEP_VALUE = 1
BERRY_VALUE = 100

# NUMBER OF PURE CLONES WITHIN A GENERATION
AMT_CLONE = 2

# AMOUNT OF TRIALS TO FIND BEST KAT
NUM_OF_TRIALS = 20 # Should be divisible by 5

# NUMBER OF GENERATIONS
NUM_SIMS = 50


# MAXIMUM STEPS PER SIMULATION
STEPS_PER_SIM = 300

# KAT'S VISION RANGE
VISION_RANGE = 1

# FIXED MAP FEATURES
WALLS_OF_DEATH  = False  # Walls are lava
WALL_PILLARS    = False  # Wall tiles periodically jut out
MAZE            = False

#HOW MANY TIMES THE MODEL WILL RUN IN A ROW
SEPERATE_MODELS = 10

#MUTATION CONSTANTS % CHANCE PER INSTRUCTION
FLIP_CHANCE = 10
ROTATE_CHANCE = 10
CHANGE_STATE_CHANCE = 10
SHIFT_CHANCE = 20
COMPOUND_CHANCE = 10
#MUTATION CONSTANTS % ABSOLUTE CHANCE
GENERATE_CHANCE = 33
SHUFFLE_CHANCE = 5
#DELETION CHANCE EXPONENTIAL
DELETE_CHANCE_EXP = 1.5
