from .. import hg_settings as hgs

class HGSettingsTestCase(object):
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