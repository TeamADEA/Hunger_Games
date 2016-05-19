import Kat
import numpy as np

MUTATION_PROBABILITY = 0.01

def mutate_kat(Kat):
    if np.random.random() < MUTATION_PROBABILITY:
        numInstr = np.size(Kat.instr_set_1)
        randomInstr = Kat.instr_set_1[np.random().randint(0, high=numInstr)]
        curMirror = randomInstr[-1]
        tempDecision = curMirror[1]
        for mirror in [-1, 0, 1, 2]:
            curMirror = randomInstr[mirror]
            nexMirror = randomInstr[mirror+1]
            curMirror[1] = nexMirror[1]
            if mirror == 2:
                curMirror[1] = tempDecision
        return Kat
    else:
        return Kat