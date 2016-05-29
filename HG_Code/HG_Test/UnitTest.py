#https://docs.python.org/2.7/library/unittest.html
#http://stackoverflow.com/questions/1322575/what-numbers-can-you-pass-as-verbosity-in-running-python-unit-test-suites
"""This is a Unit Test class for testing Hunger Game Simulation
"""
import unittest
#from .. import Mutate as mu
#import Model as mo  #not running model
#from .. import Kat
#from .. import Visualize 
#from .. import SimManager
#from .. import Hunger_Grid 
#from .. import hg_settings as hgs
import test_kat
import test_mutate
import test_sim_manager
import test_hunger_grid
import test_hg_settings
import test_model

#import copy 
#import numpy as np

class TestCaseSuperClass(unittest.TestCase):
    def setUp(self):
        pass
        
#class VisualizeTestCase(TestCaseSuperClass):
#    def runTest(self):
#        pass

class SuperClassTests(TestCaseSuperClass): pass
class KatTests(TestCaseSuperClass, test_kat.KatTestCase): pass
class MutateTests(TestCaseSuperClass, test_mutate.MutateTestCase): pass
class SimManagerTests(TestCaseSuperClass, test_sim_manager.SimManagerTestCase): pass
class HungerGridTests(TestCaseSuperClass, test_hunger_grid.HungerGridTestCase): pass
class HGSettingsTests(TestCaseSuperClass, test_hg_settings.HGSettingsTestCase): pass
class ModelTests(TestCaseSuperClass, test_model.ModelTestCase): pass

class Run_Unit_Test(object):
    def run_test(self):
        #verbosity_On = True
        verbosity_On = False
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(SuperClassTests))
        suite.addTest(unittest.makeSuite(KatTests))
        #suite.addTest(unittest.makeSuite(VisualizeTestCase))
        suite.addTest(unittest.makeSuite(SimManagerTests))
        suite.addTest(unittest.makeSuite(HungerGridTests))
        suite.addTest(unittest.makeSuite(HGSettingsTests))
        suite.addTest(unittest.makeSuite(MutateTests))
        suite.addTest(unittest.makeSuite(ModelTests))

        if verbosity_On:
            unittest.TextTestRunner(verbosity=2).run(suite)
        else:
            unittest.TextTestRunner(verbosity=1).run(suite)