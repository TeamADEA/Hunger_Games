from .. import Mutate as mu
from .. import Kat

class MutateTestCase(object):
    """Testing mutate functions.
    """
    
    def test_mutate_change_state(self):
        """Test to see if mutate does change the state of mirrors.
        """
        self.kat = Kat.Kat()
        mu.generate_behavior(self.kat)
        for i in range(4):
            newPlaceState = (self.kat.instruction_set_1[0][i][0][2])
        #self.kat.instruction_set_1[
    
    def test_mutate_rotate(self):
        """Test to see if mutate does rotate decisions.
        """
        pass
        
    def test_mutate_flip(self):
        """Test to see if mutate does flip decisions.
        """
        pass
    
    def test_mutate_create_compound(self):
        """Test to see if mutate does create a compound out of lower instructions.
        """
        pass
    
    def test_mutate_generate_behavior(kat):
        """Test to see if mutate does generate a new behavior.
        """
        pass