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
from hg_settings import *

class TestCaseSuperClass(unittest.TestCase):
    def setUp(self):
        pass
        
class KatTestCase(TestCaseSuperClass):
    def runTest(self):
        pass

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
    def runTest(self):
        pass
        
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