from .. import Hunger_Grid 

class HungerGridTestCase(object):
    """Testing Hunger_Grid clas
    """
    
    def test_hunger_grid_init(self):
        """Test to see if hunger grid is initialized properly
        """
        self.grid = Hunger_Grid.hunger_grid()
        self.assertIsInstance(self.grid.hung_grid, Hunger_Grid.hunger_grid(), \
        "not an instance of hunger_grid")
        
    def test_hunger_grid_create(self):
        pass
        
    def test_hunger_grid_get(self):
        pass