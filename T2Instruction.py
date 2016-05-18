import numpy.random as ra
import numpy as np
import T1Instruction
MUTATE_CHANCE = .01
ALLOWED_ROLLS = [0,2,4,6] #To make sure the Rolls don't make [0,0], [-1,1] possible


class T2Instruction:
    move_array = np.zeros(shape=(4,2))
    save_array = np.zeros(shape=(4,2))

    compound1 = 0
    compound2 = 0
    
    def __init__(self, cond1, x1, y1, cond2, x2, y2):
        # Condidtion (Grass:0|Lava:1|Berry:2|Kat:3|Wall:4)
        self.compound1 = T1Instruction(cond1, x1, y1)
        self.compount2 = T1Instruction(cond2, x2, y2)
        
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
        temp, compound1Check = self.compound1.check(grid, katX, katY)
        temp, compound2Check = self.compound2.check(grid, katX, katY)
        if(compound1Check and compound2Check):    
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