import Kat
import numpy as np
import random
from hg_settings import *

MUTATE_DEBUG = False # used for debug purposes
# Assume mutation of only one instruction (default) from each set
def mutate_kat(kat):
    """Mutate the Kat agent by changing its instruction.
    """
    inst_size = len(kat.instruction_set_1)
    
    generate_behavior(kat, GENERATE_CHANCE)
    if(inst_size > 0 ):
        change_state(kat, CHANGE_STATE_CHANCE, inst_size)
        rotate(kat, ROTATE_CHANCE, inst_size)
        flip(kat, FLIP_CHANCE, inst_size)
        shuffle_instructions(kat, SHUFFLE_CHANCE)
        shift_instructions(kat, SHIFT_CHANCE)
        delete_behavior(kat.instruction_set_1, DELETE_CHANCE_EXP)
    else:
        generate_behavior(kat, 100)

def change_state(kat, chance_per_instruction, instruction_1_size):
    """Mutate function that will randomly reasign the state of the given number
    of instructions.
    """
    num_mutate = 0
    for i in range(instruction_1_size):
        if(np.random.randint(0,100) <= chance_per_instruction):
            num_mutate += 1
    
    rand_chosen_instr_set1 = np.random.randint(0, high=instruction_1_size, size=num_mutate)
    for instruction in rand_chosen_instr_set1:
        newState = np.random.randint(0,5)
        for i in range(4):
            newTuple = (kat.instruction_set_1[instruction][i][0][0][0], \
            kat.instruction_set_1[instruction][i][0][0][1], newState)
            kat.instruction_set_1[instruction][i][0][0] = newTuple


def rotate(kat, chance_per_instruction, instruction_1_size):
    """Mutate function that will randomly rotate the decision of
    the given number of instructions.
    """
    
    num_mutate = 0
    for i in range(len(kat.instruction_set_1)):
        if(np.random.randint(0,100) <= chance_per_instruction):
            num_mutate += 1
    # Getting the size of the instruction set and choose instructions
    # randomly to mutate.
    rand_chosen_instr_set1 = np.random.randint(0, high=instruction_1_size, size=num_mutate)
    #NOTE: this is rotation mutation
    for instruction in rand_chosen_instr_set1:
        #saving last mirror
        temp_decision_set1 = kat.instruction_set_1[instruction][-1][1]
        #rotate from (second from last) to (last), (third from last) to (second from last),
        #(fourth from last) (i.e. first) to (third from last)
        for mirror in [2, 1, 0, -1]:
            kat.instruction_set_1[instruction][mirror+1][1] = \
            kat.instruction_set_1[instruction][mirror][1]
            #put the temp decision before for second for loop back in
            if mirror == -1:
                kat.instruction_set_1[instruction][mirror+1][1] = temp_decision_set1

def flip(kat,chance_per_instruction, instruction_1_size):
        """Mutate function that will randomly flip the decision of the
        number given number of instructions.
        
        this function is pretty old and was built when we only had a rudimentary 
        understanding of how instruction sets would pan out.
        
        it could use some cleaning up
        """
        num_mutate = 0
        for i in range(len(kat.instruction_set_1)):
            if(np.random.randint(0,100) <= chance_per_instruction):
                num_mutate += 1
                
        rand_chosen_instr_set1 = np.random.randint(0, high=instruction_1_size, size=num_mutate)
        for instruction in rand_chosen_instr_set1:
            #saving first mirror
            temp_decision_set1 = kat.instruction_set_1[instruction][0][1]

            #first time switch first with third, second time switch second with
            #fourth mirror
            for mirror in [0, 1]:
                if mirror == 1:
                    #saving second mirror
                    temp_decision_set1 = kat.instruction_set_1[instruction][1][1]

                #swith first with third mirror
                kat.instruction_set_1[instruction][mirror][1] = \
                kat.instruction_set_1[instruction][mirror+2][1]
                kat.instruction_set_1[instruction][mirror+2][1] = \
                temp_decision_set1

def create_compound(kat, num_mutate, instruction_1_size):
    """Create new compound instruction.
    Combination of two lower tier instruction into one higher level
    instruction.
    """
    while True:
        temp_instr = np.random.randint(0, high=instruction_1_size, size=2)
        if temp_instr[0] != temp_instr[1]:
            break

    temp_instr_1 = kat.instruction_set_1[temp_instr[0]]
    temp_instr_2 = kat.instruction_set_1[temp_instr[1]]
    #                   Place/state of 1st|Place/state of second|Decision of first
    new_instruction = [[[temp_instr_1[0][0][0],temp_instr_2[0][0][0]],temp_instr_1[0][1],0],\
                       [[temp_instr_1[1][0][0],temp_instr_2[1][0][0]],temp_instr_1[1][1],1],\
                       [[temp_instr_1[2][0][0],temp_instr_2[2][0][0]],temp_instr_1[2][1],2],\
                       [[temp_instr_1[3][0][0],temp_instr_2[3][0][0]],temp_instr_1[3][1],3]]
    #print new_instruction
    kat.instruction_set_2.append(new_instruction)

#def shuffle_instructions(kat):
#    """Shuffle instructions in each set.
#    """
#    np.random.shuffle(kat.instruction_set_1)
#    np.random.shuffle(kat.instruction_set_2)
#    np.random.shuffle(kat.instruction_set_3)

#def generate_behavior(kat):
#    """Generate a new behavior
#    Unlike the generate_behavior method in Kat, the state is randomly chosen.
#    """
#    yGrab, xGrab = 0, 0
#    while (yGrab,xGrab) == (0,0):
#        yGrab = random.randint(-VISION_RANGE,VISION_RANGE)
#        xGrab = random.randint(-VISION_RANGE,VISION_RANGE)
#    init_decision = random.randint(0,3)
#    state = random.randint(0,4)
#    new_instruction = [[[( yGrab,  xGrab, state)],init_decision,0],\
#                        [[( xGrab, -yGrab, state)],(init_decision+1)%4,1],\
#                        [[(-yGrab, -xGrab, state)],(init_decision+2)%4,2],\
#                        [[(-xGrab,  yGrab, state)],(init_decision+3)%4,3]]
#    kat.instruction_set_1.append(new_instruction)

def shuffle_instructions(kat, chance):
    """
    chance is the absolute chance of shuffling
    
    Shuffle instructions in each set.
	"""
    if(np.random.randint(0,100) <= chance):
        np.random.shuffle(kat.instruction_set_1)
        np.random.shuffle(kat.instruction_set_2)
        np.random.shuffle(kat.instruction_set_3)

def shift_instructions(kat, chance_per_instruction):
    """
    chance_per_instruction = 5 for 5% chance
    
    this function goes through each instruction
    in each set for the given kat, and based on the chance_per_instruction
    variable will randomly swap instructions with the one above it or below it.
    
    The purpose of this function is to give the kat a smother an easier way
    to increase fitness through reordering instructions"""
    for i_set in [kat.instruction_set_1,kat.instruction_set_2]:
        if(len(i_set) > 1):
            for i in range(len(i_set)):
                roll = np.random.randint(0,100)
                if MUTATE_DEBUG:
                    print (roll)
                if(roll <= chance_per_instruction):
                    direction = np.random.randint(0,2)
                    if(direction == 0):
                        direction = -1
                    if(i == 0):
                        direction = 1
                    if(i == (len(i_set) - 1)):
                        direction = -1
                    if MUTATE_DEBUG:
                        print (i), direction
                    temp = i_set[(i + direction)]
                    i_set[i+direction] = i_set[i]
                    i_set[i] = temp
    
def generate_behavior(kat, chance):
    """
    chance is the absolute chance of generating a new behavior
    
    Generate a new behavior
	Unlike the generate_behavior method in Kat, the state is randomly chosen.
	"""
    if(np.random.randint(0,100) <= chance):
        yGrab, xGrab = 0, 0
        while (yGrab,xGrab) == (0,0):
            yGrab = random.randint(-VISION_RANGE,VISION_RANGE)
            xGrab = random.randint(-VISION_RANGE,VISION_RANGE)
        init_decision = random.randint(0,3)
        state = random.randint(0,4)
        new_instruction = [[[( yGrab,  xGrab, state)],init_decision,0],\
                            [[( xGrab, -yGrab, state)],(init_decision+1)%4,1],\
                            [[(-yGrab, -xGrab, state)],(init_decision+2)%4,2],\
                            [[(-xGrab,  yGrab, state)],(init_decision+3)%4,3]]
        kat.instruction_set_1.insert(0,new_instruction)
    
def delete_behavior(i_set, chance_exponent):
    """
    chance_per_instruction = 5 for 5% chance
    i_set = instruction set of a kat
    
    this function iterates through each instruction in the set
    and will randomly delete instructions based on the chance given.
    """
    chance = 2
    i = 0
    while(i < len(i_set)):
        if(np.random.randint(0,100) <= chance):
            i_set.pop(i)
            if MUTATE_DEBUG:
                print (chance),i
            return
        else:
            chance *= chance_exponent
            i += 1
