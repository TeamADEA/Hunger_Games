import numpy.random as ra
import numpy as np

MUTATE_CHANCE = .01
ALLOWED_ROLLS = [0,2,4,6] #To make sure the Rolls don't make [0,0], [-1,1] possible


class T1Instruction:
    move_array = np.zeros(shape=(4,2))
    save_array = np.zeros(shape=(4,2))
    condition = 0
    x = 0
    y = 0
    
    def __init__(self, condidtion1, cond1x, cond1y):
        # Condidtion (Grass:0|Lava:1|Berry:2|Kat:3|Wall:4)
        self.condition = condidtion1 
        self.x = cond1x # Relative X location of condition
        self.y = cond1y # Relative Y location of condition
        
        self.save_array[0] = ([1,0])     #Right
        self.save_array[1] = ([0,1])     #Down
        self.save_array[2] = ([-1,0])    #Left
        self.save_array[3] = ([0,-1])    #Up
        
        #Pick random 'primary' direction
        self.save_array = np.roll(self.save_array, ra.choice(ALLOWED_ROLLS))
        
        #pick random 'primary' direction
        #ra.shuffle(self.save_array) # <- if we DO NOT care about order
        
        
        self.move_array = self.save_array
    
    def check(self, grid, katX, katY):
        if(grid[katX+self.x][katY+self.y] == self.condition):
            # Return Decision, and True if needed by Kat logic
            return self.move_array[0], True 
        # Return Do nothing and False if needed by Kat Logic
        return [0,0], False           
    
    def shuffle(self):
        ra.shuffle(self.move_array)
    
    def mutate(self):
        if (ra.rand() < MUTATE_CHANCE):
            self.save_array = np.roll(self.save_array, 2)
        self.move_array = self.save_array

test = T1Instruction(0,0,0)


