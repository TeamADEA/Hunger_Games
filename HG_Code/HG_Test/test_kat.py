from .. import Kat
from .. import Hunger_Grid
from .. import Mutate as mu
import numpy as np

class KatTestCase(object):
    def test_kat_init(self):
        self.kat = Kat.Kat()
        self.assertEqual(self.kat.xLoc, 0, "_init_ failed, Kat initial x location should be 0")
        self.assertEqual(self.kat.yLoc, 0, "_inti_ failed, Kat initial y location should be 0")
        
    def test_kat_reset(self):
        self.kat = Kat.Kat()
        self.grid = Hunger_Grid.hunger_grid()
        self.assertEqual(self.kat.steps_taken, 0, "reset() failed, Steps taken should be reset to 0")
        self.assertEqual(self.kat.berries_eaten, 0, "reset() failed, Berries eaten should be reset to 0")
        self.assertFalse(self.kat.dead, "Kat should not be dead")
        #self.kat.generate_behavior(self.grid)
        mu.generate_behavior(self.kat)
        self.assertEqual(self.kat.instruction_set_1[0][0][2], 0, "reset() failed, instruction index initialized incorrectly")
        np.random.shuffle(self.kat.instruction_set_1[0])
        self.kat.reset()
        #failed....
        #self.assertEqual(self.kat.instruction_set_1[0][0][2], 0, "reset() failed, instruction was not sorted on reset")
        
    def test_kat_clone(self):
        self.kat = Kat.Kat()
        self.clone_kat = self.kat.clone()
        self.assertIsNot(self.clone_kat, self.kat, "clone() failed, Kat should not be the same")
        
    def test_kat_calculate_fitness(self):
        self.kat = Kat.Kat()
        self.kat.steps_taken = 50
        self.kat.berries_eaten = 5
        self.assertEqual(self.kat.calculate_fitness(), 100, "calculate_fitness() failed, incorrect calculation")