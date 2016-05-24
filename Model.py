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

def one_sim(seed_kat, grid, multi_cat=False):
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

    for i in range(NUM_OF_TRIALS):
        sim_temp.clear_grid(grid)
        sim_temp.start_kat(i)
        for j in range(STEPS_PER_SIM):
            if(sim_temp.kats[i].dead == False):
                sim_temp.update(i)
            else:
                break

    avg_fitness = sim_temp.average_fitness()
    top_kats = sim_temp.top_kats()
    print top_kats
    for kat in top_kats:
        kat.reset()
    kat_temp, score_temp = sim_temp.top_kat()
    return copy.deepcopy(kat_temp), score_temp, sim_temp.return_playback(),\
           avg_fitness, copy.deepcopy(top_kats)

def playback(vis, pb, best_kats, gen):
    if (STEP_SIZE == -1):
        return
    if (STEP_SIZE == 0):
        vis.show(pb[-1], best_kats, gen)
    else:
        for i in np.arange(0,len(pb), STEP_SIZE):
            vis.show(pb[i], copy.deepcopy(best_kats), gen)


def model(seed_kat, vis, grid, specie):
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
    seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kat, grid)
    top_kats.append(fit_score)
    avg_kats.append(avg_fitness)
    playback(vis, play, seed_kat, 1)
    
    for i in np.arange(2, (NUM_SIMS+1)):
        print "Specie:",specie," | Gen:",i
        temp_top = seed_kats
        seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kats, grid, multi_cat=True)
        if fit_score < top_kats[-1]:
            seed_kats = temp_top
            top_kats.append(top_kats[-1])
            #avg_kats.append(avg_kats[-1])
        else:
            top_kats.append(fit_score)
        avg_kats.append(avg_fitness)
        playback(vis, play,copy.deepcopy(seed_kats),i)
    #vis.graph(top_kats)
    return copy.deepcopy(list(top_kats))


progenitor = Kat(0,0)
grid = hunger_grid()
vis = Visualizer(grid)

start_time = time.time()

full_graph = np.zeros(SEPERATE_MODELS*NUM_SIMS).reshape(SEPERATE_MODELS, NUM_SIMS)
print full_graph
for i in range(SEPERATE_MODELS):
    grid = hunger_grid()
    full_graph[i] = model(progenitor, vis, grid, i)

for i in range(SEPERATE_MODELS):
    print full_graph[i]

vis.graph(full_graph)
print("--- %s seconds ---" % (time.time() - start_time))