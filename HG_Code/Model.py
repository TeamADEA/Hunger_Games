import numpy as np
import copy
import time
from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
from Hunger_Grid import hunger_grid





STEP_SIZE = -1 # 0 = only last frame,
                # 1 = every frame,
                # N = every N frames
                # -1 = don't show

tki_breakdown = np.zeros(NUM_OF_GENERATIONS*6).reshape(NUM_OF_GENERATIONS, 6)
full_graph = np.zeros(NUM_OF_SPECIES*NUM_OF_GENERATIONS).reshape(NUM_OF_SPECIES, NUM_OF_GENERATIONS)
full_graph_bk = np.zeros(NUM_OF_SPECIES*2).reshape(NUM_OF_SPECIES, 2)

def run_model(from_lava = .02, to_lava = .02, from_berry = .05, to_berry = .05, t_name = 'Default'):
    progenitor = Kat(0,0)
    grid = hunger_grid()
    vis = Visualizer(grid)
    start_time = time.time()
    lava_chance_array = np.arange(1, NUM_OF_SPECIES+1, dtype='float')
    berry_chance_array = np.arange(1, NUM_OF_SPECIES+1, dtype='float')
    
    # SETUP LAVA AND BERRY AMOUNTS
    if(from_lava == to_lava): # NO CHANGE IN LAVA AMOUNTS. SET ALL TO 1 VALUE
        lava_chance_array[:] = from_lava
    else: #CHANGE IN LAVA AMOUNT, CALCULATE STEP SIZE OF LAVA
        inc = (to_lava - from_lava) / NUM_OF_SPECIES
        lava_chance_array = np.arange(from_lava, to_lava, inc)
    if(from_berry == to_berry): # NO CHANCE IN BERRY AMOUNTS. SET ALL TO 1 VALUE
        berry_chance_array[:] = from_berry
    else: # CHANGE IN BERRY AMOUNT, CALCULATE STEP SIZE OF BERRY
        inc = (to_berry - from_berry) / NUM_OF_SPECIES
        berry_chance_array = np.arange(from_berry, to_berry, inc)
    
    for i in range(NUM_OF_SPECIES): # MAIN LOOP OF SIMULATION RUNNING
        grid = hunger_grid(lava_chance_array[i], berry_chance_array[i])
        full_graph[i] = model(progenitor, vis, grid, i, t_name)
        full_graph_bk[i] = [grid.lava_chance, grid.berry_chance]
    
    # DISPLAY VARIOUS GRAPHS AND PLOTS
    tki_breakdown[:] /= NUM_OF_SPECIES
    vis.graph(full_graph, full_graph_bk, t_name)
    vis.ins_graph(tki_breakdown, t_name)
    vis.chance_vs_fitness(full_graph, full_graph_bk, t_name)
    print("--- %s MODEL COMPLETE ---" % (t_name))
    print("--- TIME TO COMPLETE MODEL: %s seconds ---" % (time.time() - start_time))
    vis.show_plots()

def one_sim(seed_kat, grid, gen , multi_cat=False):
    """Run one simulation of number of time steps (default: 300)

    First initialize a sim_manager with first Kat agent.
	Then update at each time steps, finally taking the top
	Kat and top fitness score, returns it.
    """
    if not multi_cat:
        sim_temp = sim_manager(seed_kat, grid)
        top_kat = seed_kat
    else:
        sim_temp = sim_manager(seed_kat, grid, multi_cat=True)
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

    for kat in top_kats:
        kat.reset()
    kat_temp, score_temp = sim_temp.top_kat()
    return copy.deepcopy(kat_temp), score_temp, sim_temp.return_playback(),\
           avg_fitness, copy.deepcopy(top_kats)

def playback(vis, pb, best_kats, gen, specie, t_name):
    if (STEP_SIZE == -1):
        return
    if (STEP_SIZE == 0):
        vis.show(pb[-1], best_kats, gen)
    else:
        for i in np.arange(0,len(pb), STEP_SIZE):
            vis.show(pb[i], copy.deepcopy(best_kats), gen, specie, t_name)


def model(seed_kat, vis, grid, specie, t_name):
    """Run multiple simulation of number of time steps each,
	(default: 300 simulations).

    In a loop, keep running each simulation of 300
	number of time steps, append the top fitness score,
	and after loops ended, graph the fitness score over
	generations (simulations).
    """
    top_kats = []
    avg_kats = []
    print "Specie:",specie," | Gen: 1"
    seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kat, grid, 0)
    top_kats.append(fit_score)
    avg_kats.append(avg_fitness)
    playback(vis, play, seed_kat, 1, specie+1, t_name)
    if (NUM_OF_SPECIES > 1):
        for i in np.arange(2, (NUM_OF_GENERATIONS+1)):
            print "\nMODEL NAME: %s" % (t_name)
            print "\n######################## START: Specie:",specie+1," | Gen:",i, "#####################"
            temp_top = seed_kats
            seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kats, grid, (i-1), multi_cat=True)
            if fit_score < top_kats[-1]:
                seed_kats = temp_top
                top_kats.append(top_kats[-1])
            else:
                top_kats.append(fit_score)
            avg_kats.append(avg_fitness)
            playback(vis, play,copy.deepcopy(seed_kats),i, specie+1, t_name)
            print "######################## END: Specie:",specie+1," | Gen:",i, "#######################\n"
    return copy.deepcopy(list(top_kats))


