import numpy as np
import copy
import time
from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
from Hunger_Grid import hunger_grid
import sys
import os



STEP_SIZE = 10 # 0 = only last frame,
                # 1 = every frame,
                # N = every N frames
                # -1 = don't show

tki_breakdown = np.zeros(NUM_OF_GENERATIONS*6).reshape(NUM_OF_GENERATIONS, 6)
full_graph = np.zeros(NUM_OF_SPECIES*NUM_OF_GENERATIONS).reshape(NUM_OF_SPECIES, NUM_OF_GENERATIONS)
full_graph_bk = np.zeros(NUM_OF_SPECIES*2).reshape(NUM_OF_SPECIES, 2)

def run_model(from_lava = .02, to_lava = .02, from_berry = .05, to_berry = .05\
                , from_mut=10, to_mut=10, from_gen = 33, to_gen = 33, \
                t_name = 'Default', frames = -1):
    global STEP_SIZE
    STEP_SIZE = frames
    progenitor = Kat(0,0)
    grid = hunger_grid()
    vis = Visualizer(grid)
    start_time = time.time()
    
    def calc_steps(from_num, to_num):
        array = np.arange(1, NUM_OF_SPECIES+1, dtype='float')
        if(from_num == to_num):
            array[:] = from_num
        else:
            inc = (float(to_num) - from_num) / float(NUM_OF_SPECIES)
            array = np.arange(from_num, to_num, inc, dtype='float')
        return copy.deepcopy(array)
    
    lava_chance_array = calc_steps(from_lava, to_lava) 
    berry_chance_array = calc_steps(from_berry, to_berry)
    mutate_chance_array = calc_steps(from_mut, to_mut)
    generate_chance_array = calc_steps(from_gen, to_gen)
    
    #open output file
    file_name = t_name + '.txt'
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    out_file = open(os.path.join(__location__,file_name), 'a')
    
    print "\n", generate_chance_array
    print mutate_chance_array
    for i in range(NUM_OF_SPECIES): # MAIN LOOP OF SIMULATION RUNNING
        mutation_var = [mutate_chance_array[i]]
        mutation_var.append(generate_chance_array[i])
        grid = hunger_grid(lava_chance_array[i], berry_chance_array[i])
        full_graph[i] = model(progenitor, vis, grid, i, mutation_var,t_name, out_file)
        full_graph_bk[i] = [grid.lava_chance, grid.berry_chance]
    
    #close output file
    out_file.close()
    # DISPLAY VARIOUS GRAPHS AND PLOTS
    tki_breakdown[:] /= NUM_OF_SPECIES
    vis.graph(full_graph, full_graph_bk, t_name)
    vis.ins_graph(tki_breakdown, t_name)
    vis.chance_vs_fitness(full_graph, full_graph_bk, mutate_chance_array, generate_chance_array,t_name)
    print("--- %s MODEL COMPLETE ---" % (t_name))
    print("--- TIME TO COMPLETE MODEL: %s seconds ---" % (time.time() - start_time))
    vis.show_plots()

def one_sim(seed_kat, grid, mut ,gen, out_file, multi_cat=False):
    """Run one simulation of number of time steps (default: 300)

    First initialize a sim_manager with first Kat agent.
	Then update at each time steps, finally taking the top
	Kat and top fitness score, returns it.
    """
    if not multi_cat:
        sim_temp = sim_manager(seed_kat, grid, mut)
        top_kat = seed_kat
    else:
        sim_temp = sim_manager(seed_kat, grid, mut, multi_cat=True)
        top_kat = seed_kat[0]

    for i in range(NUM_OF_INDIVIDUALS):
        sim_temp.clear_grid(grid)
        sim_temp.start_kat(i)
        for j in range(STEPS_PER_SIM):
            if(sim_temp.kats[i].dead == False):
                sim_temp.update(i, j)
            else:
                break

    avg_fitness = sim_temp.average_fitness()
    top_kats = sim_temp.top_kats() # ARRAY FOR DISPLAYING FITNESS
    tki_breakdown[gen] += sim_temp.tk_breakdown() # FOR BREAKDOWN OF INSTRUCTIONS

    #file output
    for k in top_kats:
        out_file.write("\nFittness: ")
        out_file.write(str(k.calculate_fitness()))
        out_file.write(k.print_ins_1(False))
    
    for kat in top_kats:
        kat.reset()
    kat_temp, score_temp = sim_temp.top_kat()
    return copy.deepcopy(kat_temp), score_temp, sim_temp.return_playback(),\
           avg_fitness, copy.deepcopy(top_kats)

def playback(vis, pb, best_kats, gen, specie, t_name):
    if (STEP_SIZE == -1):
        return
    if (STEP_SIZE == 0):
        vis.show(pb[-1], best_kats, gen, specie, t_name)
    else:
        for i in np.arange(0,len(pb), STEP_SIZE):
            vis.show(pb[i], copy.deepcopy(best_kats), gen, specie, t_name)


def model(seed_kat, vis, grid, specie, mut,t_name, out_file):
    """Run multiple simulation of number of time steps each,
	(default: 300 simulations).

    In a loop, keep running each simulation of 300
	number of time steps, append the top fitness score,
	and after loops ended, graph the fitness score over
	generations (simulations).
    """
    top_kats = []
    avg_kats = []
    print "Species:",specie," | Gen: 1"
    seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kat, grid, mut, 0,out_file)
    top_kats.append(fit_score)
    avg_kats.append(avg_fitness)
    playback(vis, play, seed_kat, 1, specie+1, t_name)
    
    #flie output
    out_file.write("Species:")
    out_file.write(str(specie))
    out_file.write(" | Gen: 1\n")
    
    if (NUM_OF_SPECIES > 1):
        
        for i in np.arange(2, (NUM_OF_GENERATIONS+1)):
            #file output
            out_file.write("\nMODEL NAME: %s" % (t_name))
            out_file.write("\n######### START: Species:")
            out_file.write(str(specie+1))
            out_file.write(" | Gen:")
            out_file.write(str(i))
            out_file.write("###########")
            
            print "\nMODEL NAME: %s" % (t_name)
            print "\n######################## START: Species:",specie+1," | Gen:",i, "#####################"
            temp_top = seed_kats
            seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kats, grid, mut, (i-1),out_file, multi_cat=True)
            if fit_score < top_kats[-1]:
                seed_kats = temp_top
                top_kats.append(top_kats[-1])
            else:
                top_kats.append(fit_score)
            avg_kats.append(avg_fitness)
            playback(vis, play,copy.deepcopy(seed_kats),i, specie+1, t_name)
            print "######################## END: Species:",specie+1," | Gen:",i, "#######################\n"
            
            #file output
            out_file.write("######### END: Species:")
            out_file.write(str(specie+1))
            out_file.write(" | Gen:")
            out_file.write(str(i))
            out_file.write("###########\n")
    return copy.deepcopy(list(top_kats))

