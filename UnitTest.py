#https://docs.python.org/2.7/library/unittest.html
#http://stackoverflow.com/questions/1322575/what-numbers-can-you-pass-as-verbosity-in-running-python-unit-test-suites
"""This is a Unit Test class for testing Hunger Game Simulation
"""
import unittest
import Mutate as mu
#import Model as mo  #not running model

from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from Hunger_Grid import hunger_grid
import hg_settings as hgs

class TestCaseSuperClass(unittest.TestCase):
    def setUp(self):
        pass
        
class KatTestCase(TestCaseSuperClass):
    def test_kat_init(self):
        self.kat = Kat()
        self.assertEqual(self.kat.xLoc, 0, "Kat initial x location is incorrect")
        self.assertEqual(self.kat.yLoc, 0, "Kat initial y location is incorrect")
        self.assertEqual(self.kat.steps_taken, 0, "Steps taken should be initialized to 0")
        self.assertEqual(self.kat.berries_eaten, 0, "Berries eaten should be initialize to 0")
        self.assertFalse(self.kat.dead, "Kat should not be dead")

class VisualizeTestCase(TestCaseSuperClass):
    def runTest(self):
        pass
        
class SimManagerTestCase(TestCaseSuperClass):
    def runTest(self):
        pass

class HungerGridTestCase(TestCaseSuperClass):
    def runTest(self):
        pass

class HGSettingsTestCase(TestCaseSuperClass):
    def test_correct_global_var(self):
        self.assertEqual(hgs.UP, 0, "Up code should be 0")
        self.assertEqual(hgs.RIGHT, 1, "Right code should be 1")
        self.assertEqual(hgs.DOWN, 2, "Down code should be 2")
        self.assertEqual(hgs.LEFT, 3, "Left code should be 3")
        self.assertEqual(hgs.DO_NOTHING, 4, "Do_nothing code should be 4")
        self.assertEqual(hgs.GRASS, 0, "Grass code should be 0")
        self.assertEqual(hgs.LAVA, 1, "Lava code should be 1")
        self.assertEqual(hgs.BERRY, 2, "Berry code should be 2")
        self.assertEqual(hgs.KAT, 3, "Kat code should be 3")
        self.assertEqual(hgs.WALL, 4, "Wall code should be 4")
        
class MutateTestCase(TestCaseSuperClass):
    def runTest(self):
        pass
        
class ModelTestCase(TestCaseSuperClass):
    def runTest(self):
        pass

verbosity_On = True
#verbosity_On = False
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCaseSuperClass))
suite.addTest(unittest.makeSuite(KatTestCase))
suite.addTest(unittest.makeSuite(VisualizeTestCase))
suite.addTest(unittest.makeSuite(SimManagerTestCase))
suite.addTest(unittest.makeSuite(HungerGridTestCase))
suite.addTest(unittest.makeSuite(HGSettingsTestCase))
suite.addTest(unittest.makeSuite(MutateTestCase))
suite.addTest(unittest.makeSuite(ModelTestCase))

if verbosity_On:
    unittest.TextTestRunner(verbosity=2).run(suite)
else:
    unittest.TextTestRunner(verbosity=1).run(suite)