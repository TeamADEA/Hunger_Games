from .. import Mutate as mu
from .. import Kat
from .. import hg_settings as hgs

class MutateTestCase(object):
    """Testing mutate functions.
    """
    
    #NOTE: since it is depended on random, there is a chance, this
    #test will fail, but it shouldn't fail multiple times
    def test_mutate_change_state(self):
        """Test to see if mutate does change the state of mirrors.
        """
        self.kat = Kat.Kat()
        mu.generate_behavior(self.kat, 100)
        for i in range(4):
            newPlaceState = (self.kat.instruction_set_1[0][i][0][0][0],
            self.kat.instruction_set_1[0][i][0][0][1], 1)
            self.kat.instruction_set_1[0][i][0][0] = newPlaceState
        self.assertEqual(self.kat.instruction_set_1[0][0][0][0][2], 1, 
        "state was setted incorrectly")
        mu.change_state(self.kat, 100, 1)
        self.assertFalse(self.kat.instruction_set_1[0][0][0][0][2] == 1, 
        "state was changed incorrectly")
    
    def test_mutate_rotate(self):
        """Test to see if mutate does rotate decisions.
        """
        self.kat = Kat.Kat()
        mu.generate_behavior(self.kat, 100)
        lastDecision = self.kat.instruction_set_1[0][-1][1]
        mu.rotate(self.kat, 100, 1)
        self.assertEqual(self.kat.instruction_set_1[0][0][1], lastDecision,
        "decision did not rotate")
        
    def test_mutate_flip(self):
        """Test to see if mutate does flip decisions.
        """
        self.kat = Kat.Kat()
        mu.generate_behavior(self.kat, 100)
        firstDecision = self.kat.instruction_set_1[0][0][1]
        mu.flip(self.kat, 100, 1)
        self.assertEqual(self.kat.instruction_set_1[0][2][1], firstDecision,
        "decision did not flip")
    
    def test_mutate_create_compound(self):
        """Test to see if mutate does create a compound out of lower instructions.
        """
        self.kat = Kat.Kat()
        mu.generate_behavior(self.kat, hgs.GENERATE_CHANCE)
        mu.generate_behavior(self.kat, hgs.GENERATE_CHANCE)