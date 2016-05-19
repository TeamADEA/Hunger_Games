import numpy.random as ra
import numpy as np
# Condition (Grass:0|Lava:1|Berry:2|Kat:3|Wall:4)
# decision code (down:0| left:1| up:2| right:3

class Kat():
    xLoc = 0
    yLoc = 0
    berriesFound = 0
    distanceTraveled = 0
    dead = False
    
    def __init__(self, x,y):
        self.xLoc = x
        self.yLoc = y
        
    def reset(self):
        distanceTraveled = 0
        berriesFound = 0
        dead = False
        
    def clone(self):
        self.reset()
        return self
        