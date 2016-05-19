import numpy.random as ra
import numpy as np
import random
from hg_settings import *
# Condition (Grass:0|Lava:1|Berry:2|Kat:3|Wall:4)
# decision code (down:0| left:1| up:2| right:3

class Kat(object):
    xLoc = 0
    yLoc = 0
    berries_eaten= 0
    steps_taken = 0
    instruction_set_1 = []
    instruction_set_2 = []
    instruction_set_3 = []
    dead = False
    
    def __init__(self, x, y):
        self.xLoc = x
        self.yLoc = y
        
    def reset(self):
        self.steps_taken = 0
        self.berries_eaten = 0
        self.dead = False
        
    def clone(self):
        self.reset()
        return self
    
    def calculate_fitness(self):
        return steps_taken + (berries_eaten * 10)
        
    # Only reads 1 instruction set at the moment
    def make_decision(self, grid):
        for instruction in self.instruction_set_1:
            for mirror in instruction:
                for plc_state in mirror[0]:
                    if not place_is_state(grid, plc_state):
                        break
                if is_valid_move(grid, mirror[1]):
                    return mirror[1] # Return its desision
                else:
                    pass #TODO Shuffle mirror
                    break
        return self.generate_behavior(grid)
        
    def place_is_state(self, grid, plc_state):
        if grid[self.yLoc + plc_state[0]][self.xLoc + plc_state[1]] == plc_state[2]:
            return True
        return False
        
    def is_valid_move(self, grid, move):
        if move == NOTHING:
            return True
        if move == DOWN:
            attempt = grid[self.yLoc+1][self.xLoc]
        elif move == RIGHT:
            attempt = grid[self.yLoc][self.xLoc+1]
        elif move == UP:
            attempt = grid[self.yLoc-1][self.xLoc]
        elif move == LEFT:
            attempt = grid[self.yLoc][self.xLoc-1]
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
        yGrab, xGrab = 0, 0
        while (yGrab,xGrab) == (0,0):      
            yGrab = random.randint(-2,2)
            xGrab = random.randint(-2,2)
        init_decision = random.randint(0,3)
        state = grid[self.yLoc + yGrab][self.xLoc + xGrab]
        instruction = [[[(yGrab,xGrab,state)],init_decision],\
                       [[(yGrab,-xGrab,state)],(init_decision+1)%4],\
                       [[(-yGrab,-xGrab,state)],(init_decision+2)%4],\
                       [[(-yGrab,xGrab,state)],(init_decision+3)%4]]
        instruction_set_1 = [instruction] + self.instruction_set_1
        return init_decision