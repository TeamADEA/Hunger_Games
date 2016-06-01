from .. import Hunger_Grid 

class HungerGridTestCase(object):
    """Testing Hunger_Grid clas
    """
    
    def test_hunger_grid_init(self):
        """Test to see if hunger grid is initialized properly
        """
        self.grid = Hunger_Grid.hunger_grid()
        self.assertIsInstance(self.grid, Hunger_Grid.hunger_grid, \
        "not an instance of hunger_grid")
        self.assertEqual(self.grid.hung_grid[0, 0], 4, "wall incorrectly placed")
        self.assertEqual(self.grid.hung_grid[-1, -1], 4, "wall incorrectly placed")
        
    def test_hunger_grid_create(self):
        """Test to see if hunger grid create what is expected
        """
        self.grid = Hunger_Grid.hunger_grid()
        self.grid.newGrid = Hunger_Grid.hunger_grid().create_hunger_grid(M=30, N=30, P_LAVA = 1.0)
        self.assertTrue(self.grid.newGrid.size == 900, "Grid size is incorrect")
        self.assertTrue(self.grid.newGrid[2, 2] == 1, "Lava chance is not acting correctly")
        self.assertTrue(self.grid.newGrid[-3, -3] == 1, "Lava chance is not acting correctly")
        
    def test_hunger_grid_get(self):
        """Test to see if hunger grid get grid does return a deepcopy.
        """
        self.grid = Hunger_Grid.hunger_grid()
        self.grid.newGrid = self.grid.get_grid()
        self.assertIsNot(self.grid.hung_grid, self.grid.newGrid, \
        "get_grid() failed, did not do a deep copy")
        