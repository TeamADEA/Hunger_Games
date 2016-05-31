from .. import SimManager
from .. import Kat
from .. import Hunger_Grid
from .. import hg_settings as hgs
import random

class SimManagerTestCase(object):
    """Testing SimManager class
    """
    def test_sim_manager_init(self):
        """Test to see if sim manager intialized properly.
        """
        self.kat = Kat.Kat()
        self.grid = Hunger_Grid.hunger_grid()
        self.sim_temp = SimManager.sim_manager(self.kat, self.grid, multi_cat=False)
        #multi_cat is on
        #self.sim_temp = SimManager.sim_manager(self.kat, self.grid, multi_cat=True)
        self.assertEqual(len(self.sim_temp.kats), hgs.NUM_OF_TRIALS, \
        "number of kat agents initialized in sim manager is incorrect")
        randomKatIndex = random.randint(0, len(self.sim_temp.kats))
        self.assertEqual(self.sim_temp.kats[randomKatIndex].xLoc, 34/2, \
        "kats initial x location is not at the center")
        self.assertEqual(self.sim_temp.kats[randomKatIndex].yLoc, 34/2, \
        "kats initial y location is not at the center")