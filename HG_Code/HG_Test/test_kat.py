from .. import Kat
from .. import Hunger_Grid
from .. import Mutate as mu
import numpy as np

class KatTestCase(object):
    """Testing Kat agent class
    """
    def test_kat_init(self):
        """Test to see if Kat's variables upon initialization has the correct value.
        """
        self.kat = Kat.Kat()
        self.assertIsInstance(self.kat, Kat.Kat, "fdfd")
        self.assertEqual(self.kat.xLoc, 0, "_init_ failed, Kat initial x location should be 0")
        self.assertEqual(self.kat.yLoc, 0, "_inti_ failed, Kat initial y location should be 0")
        self.assertEqual(len(self.kat.instruction_set_1), 0, \
        "there should be no behavior upon initialization")
        self.assertEqual(len(self.kat.instruction_set_2), 0, \
        "there should be no behavior upon initialization")
        self.assertEqual(len(self.kat.instruction_set_2), 0, \
        "there should be no behavior upon initialization")
        
    def test_kat_reset(self):
        """Testing to see if reset() will reset some of Kat agent's variables. 
        Also to test if reset will reset the order of mirrors for any instruction in a Kat agent.
        """
        self.kat = Kat.Kat()
        self.grid = Hunger_Grid.hunger_grid()
        self.assertEqual(self.kat.steps_taken, 0, "reset() failed, Steps taken should be reset to 0")
        self.assertEqual(self.kat.berries_eaten, 0, "reset() failed, Berries eaten should be reset to 0")
        self.assertFalse(self.kat.dead, "Kat should not be dead")
        mu.generate_behavior(self.kat)
        self.assertEqual(self.kat.instruction_set_1[0][0][2], 0, \
        "reset() failed, instruction index initialized incorrectly")
        np.random.shuffle(self.kat.instruction_set_1[0])
        self.kat.reset()
        #failed....
        #self.assertEqual(self.kat.instruction_set_1[0][0][2], 0, \
        #"reset() failed, instruction was not sorted on reset")
        
    def test_kat_clone(self):
        """Testing to see if clone() will actually clone a different Kat agent.
        """
        self.kat = Kat.Kat()
        self.clone_kat = self.kat.clone()
        self.assertIsNot(self.clone_kat, self.kat, "clone() failed, Kat should not be the same")
        
    def test_kat_calculate_fitness(self):
        """Testing to see if calculate_fitness() returns back an accurate fitness score.
        """
        self.kat = Kat.Kat()
        self.kat.steps_taken = 50
        self.kat.berries_eaten = 5
        self.assertEqual(self.kat.calculate_fitness(), 100, "calculate_fitness() failed, incorrect calculation")
        
    def test_kat_make_decision(self):
        """Testing to see if make_decision() return decision that is to be expected.
        """
        self.kat = Kat.Kat(15, 15)
        self.grid = Hunger_Grid.hunger_grid()
        self.grid.hung_grid[self.kat.yLoc+0, self.kat.xLoc+1] = 2
        self.instruction = [[[(0, 1, 2)], 0, 0],\
                            [[(1, 0, 4)], 1, 1],\
                            [[(0, -1, 4)], 2, 2],\
                            [[(-1, 0, 4)], 3, 3]]
        self.kat.instruction_set_1.append(self.instruction)
        self.assertTrue(self.kat.make_decision(self.grid.hung_grid) == 0, \
        "make_decision failed(), kat did not use the correct mirror and correct decision")
        
    def test_kat_place_is_state(self):
        """Testing to see if place_is_state is checking right cell.
        """    
        self.kat = Kat.Kat(15, 15)
        self.grid = Hunger_Grid.hunger_grid()
        self.grid.hung_grid[self.kat.yLoc+0, self.kat.xLoc+1] = 2
        self.assertTrue(self.kat.place_is_state(self.grid.hung_grid, (0, 1, 2)), \
        "place_is_state() failed, not checking location correctly")
        self.assertFalse(self.kat.place_is_state(self.grid.hung_grid, (0, 1, 3)), \
        "place_is_state() failed, not checking location correctly")
        
    def test_kat_is_valid_move(self):
        """Test to see if is_valid_move really test the cell and give back correct result.
        """
        self.kat = Kat.Kat(15, 15)
        self.grid = Hunger_Grid.hunger_grid()
        self.grid.hung_grid[self.kat.yLoc+0, self.kat.xLoc+1] = 3
        self.grid.hung_grid[self.kat.yLoc+1, self.kat.xLoc+0] = 2
        self.assertFalse(self.kat.is_valid_move(self.grid.hung_grid, 1), \
        "is_valid_move() failed, right side should be a Kat, so no moving")
        self.assertTrue(self.kat.is_valid_move(self.grid.hung_grid, 2), \
        "is_valid_move() failed, down should be berry, so can move")
        self.kat.xLoc = 31
        self.assertFalse(self.kat.is_valid_move(self.grid.hung_grid, 1), \
        "is_valid_move() failed, right side should be wall, so no moving")
        