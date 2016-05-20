import Kat
import numpy as np
import numpy.random as ra

#assume mutation of only one instruction (default) from each set
def mutate_kat(Kat, numOfMutateInstr=1, mutate_prob=0.01):
    if ra.random() < mutate_prob:
        num_instr_to_mutate = numOfMutateInstr
        
        num_Instr_in_set1 = np.size(Kat.instruction_set_1)
        rand_chosen_instr_set1 = Kat.instruction_set_1[ra.randint(0, high=num_Instr_in_set1, size=num_instr_to_mutate)]
        
        num_Instr_in_set2 = np.size(Kat.instruction_set_2)
        rand_chosen_instr_set2 = Kat.instruction_set_1[ra.randint(0, high=num_Instr_in_set2, size=num_instr_to_mutate)]

        num_Instr_in_set3 = np.size(Kat.instruction_set_3)
        rand_chosen_instr_set3 = Kat.instruction_set_1[ra.randint(0, high=num_Instr_in_set3, size=num_instr_to_mutate)]

        
        for instruction in xrange(num_instr_to_mutate):
            #NOTE: this is rotation mutation
            #saving last mirror
            temp_decision_set1 = rand_chosen_instr_set1[instruction][-1][1]
            temp_decision_set2 = rand_chosen_instr_set2[instruction][-1][1]
            temp_decision_set3 = rand_chosen_instr_set3[instruction][-1][1]
            #rotate from (second from last) to (last), (third from last) to (second from last),
            #(fourth from last) (i.e. first) to (third from last)
            for mirror in [2, 1, 0, -1]:
                rand_chosen_instr_set1[instruction][mirror+1][1] = \
                rand_chosen_instr_set1[instruction][mirror][1]
                
                rand_chosen_instr_set2[instruction][mirror+1][1] = \
                rand_chosen_instr_set2[instruction][mirror][1]
                
                rand_chosen_instr_set3[instruction][mirror+1][1] = \
                rand_chosen_instr_set3[instruction][mirror][1]
                #put the temp decision before for second for loop back in
                if mirror == -1:
                    rand_chosen_instr_set1[instruction][mirror+1][1] = temp_decision_set1
                    
                    rand_chosen_instr_set2[instruction][mirror+1][1] = temp_decision_set2
                    
                    rand_chosen_instr_set3[instruction][mirror+1][1] = temp_decision_set3
        
        #NOTE: this is flip mutation
        #for instruction in xrange(num_instr_to_mutate):
            ##saving first mirror
            #temp_decision_set1 = rand_chosen_instr_set1[instruction][0][1]
            #temp_decision_set2 = rand_chosen_instr_set2[instruction][0][1]
            #temp_decision_set3 = rand_chosen_instr_set3[instruction][0][1]
            
            ##first time switch first with third, second time switch second with
            ##fourth mirror
            #for mirror in [0, 1]:
                #if mirror == 1:
                    ##saving second mirror
                    #temp_decision_set1 = rand_chosen_instr_set1[instruction][1][1]
                    #temp_decision_set2 = rand_chosen_instr_set2[instruction][1][1]
                    #temp_decision_set3 = rand_chosen_instr_set3[instruction][1][1]
            ##swith first with third mirror
            #rand_chosen_instr_set1[instruction][mirror][1] = \
            #rand_chosen_instr_set1[instruction][mirror+2][1]
            #rand_chosen_instr_set1[instruction][mirror+2][1] = \
            #temp_decision_set1
            
            #rand_chosen_instr_set2[instruction][mirror][1] = \
            #rand_chosen_instr_set2[instruction][mirror+2][1]
            #rand_chosen_instr_set2[instruction][mirror+2][1] = \
            #temp_decision_set2

            #rand_chosen_instr_set3[instruction][mirror][1] = \
            #rand_chosen_instr_set3[instruction][mirror+2][1]
            #rand_chosen_instr_set3[instruction][mirror+2][1] = \
            #temp_decision_set3       
