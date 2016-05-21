import random
import numpy as np 
import copy
from hg_settings import *
# Condition (Grass:0| Lava:1| Berry:2| Kat:3| Wall:4)
# Decision Code (down:0| left:1| up:2| right:3)

class Kat(object):
    """Create and manage a Kat agent.
    
    Attributes
    ----------
    x : int
        The x location of the Kat agent.

    y : int
        The y location of the Kat agent.
    
    Other Attributes
    ----------------
    berries_eaten : int
        The number of berries that Kat agent has ate.
    
    steps_taken : int
        The number of steps that Kat agent has walked.
        
    instruction_set_1 : list
        A list of tier 1 instructions that Kat agent has.
    
    instruction_set_2 : list
        A list of tier 2 instructions that Kat agent has.
    
    instruction_set_3: list
        A list of tier 3 instructions that Kat agent has.
    
    dead : boolean
        A boolean value that indicate if the Kat agent is dead.
    """
    def __init__(self, x=0, y=0):
        self.xLoc = x
        self.yLoc = y
        self.berries_eaten = 0
        self.steps_taken = 0
        self.instruction_set_1 = []
        self.instruction_set_2 = []
        self.instruction_set_3 = []
        self.dead = False
        
    def reset(self):
        """Reset the Kat agent's attributes.
        
        Attributes resettable are steps_taken, berries_eaten, and dead.
        """
        self.steps_taken = 0
        self.berries_eaten = 0
        self.dead = False
        
    def clone(self):
        self.reset()
        clone = copy.deepcopy(self)
        return clone
    
    def calculate_fitness(self):
        """Calculate the fitness value of this Kat agent.
        
        The metrics to consider are the number of steps the Kat 
        agent has taken and the amount of berries eaten.
        """
        return self.steps_taken + (self.berries_eaten * 10)
        
    # Only reads 1 instruction set at the moment
    def make_decision(self, grid):
        """The Kat makes a decision on its next move.
        
        This function works with SimManager module.
        Kats goes through list of instructions at each level
        and check if the any of the condition (place & state)
        is valid and the decision is a valid decision. If 
        decision is not valid, shuffle the mirrors in that
        instruction and generate a new behavior.
        """
        for instruction in self.instruction_set_1:
            for mirror in instruction:
                for plc_state in mirror[0]:
                    if not self.place_is_state(grid, plc_state):
                        break
                if self.is_valid_move(grid, mirror[1]):
                    return mirror[1] # Return its decision
                else:
                    np.random.shuffle(instruction) # Shuffle mirror
                    break
        return self.generate_behavior(grid)
        
    def place_is_state(self, grid, plc_state):
        """Check if the place (i.e. cell on a grid) is one of
        the expected state.
        """
        if (grid[(self.yLoc + plc_state[0]), (self.xLoc + plc_state[1])] == plc_state[2]):
            return True
        return False
        
    def is_valid_move(self, grid, move):
        """Check if the move is a valid move. If the
        desired spot is a wall or another Kat agent, 
        it is considered an invalid move.
        """
        if move == DOWN:
            attempt = grid[self.yLoc+1, self.xLoc]
        elif move == RIGHT:
            attempt = grid[self.yLoc, self.xLoc+1]
        elif move == UP:
            attempt = grid[self.yLoc-1, self.xLoc]
        elif move == LEFT:
            attempt = grid[self.yLoc, self.xLoc-1]
        else:
            raise Exception("Move was an invalid code.")
        if attempt == WALL or attempt == KAT:
            return False
        else:
            return True
    
    def take_step(self,yLoc,xLoc):
        self.yLoc = yLoc
        self.xLoc = xLoc
        self.steps_taken +=  1
        
    def die(self):
        self.dead = True
    
    def eat_berry(self):
        self.berries_eaten += 1
    
    def generate_behavior(self, grid):
        """Generate a new behavior for the Kat agent.
        
        A cell is randomly selected with the state at
        that cell recorded. A new instruction is then 
        created with the coordinates and the state.
        A decision for first mirror is randomly selected
        with other decision being mirrored decision.
        The new instruction becomes the Kat's first 
        priority instruction.
        """
        yGrab, xGrab = 0, 0
        while (yGrab,xGrab) == (0,0):      
            yGrab = random.randint(-2,2)
            xGrab = random.randint(-2,2)
        init_decision = random.randint(0,3)
        state = grid[self.yLoc + yGrab][self.xLoc + xGrab]
        instruction = [[[( yGrab,  xGrab, state)],init_decision],\
                       [[( yGrab, -xGrab, state)],(init_decision+1)%4],\
                       [[(-yGrab, -xGrab, state)],(init_decision+2)%4],\
                       [[(-yGrab,  xGrab, state)],(init_decision+3)%4]]
        self.instruction_set_1 = [instruction] + self.instruction_set_1
        return init_decision