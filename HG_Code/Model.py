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

tki_breakdown = np.zeros(NUM_SIMS*6).reshape(NUM_SIMS, 6)
full_graph = np.zeros(SEPERATE_MODELS*NUM_SIMS).reshape(SEPERATE_MODELS, NUM_SIMS)
full_graph_bk = np.zeros(SEPERATE_MODELS*2).reshape(SEPERATE_MODELS, 2)

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

    for i in range(NUM_OF_TRIALS):
        sim_temp.clear_grid(grid)
        sim_temp.start_kat(i)
        for j in range(STEPS_PER_SIM):
            if(sim_temp.kats[i].dead == False):
                sim_temp.update(i)
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
    seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kat, grid, 0)
    top_kats.append(fit_score)
    avg_kats.append(avg_fitness)
    playback(vis, play, seed_kat, 1)
    if (SEPERATE_MODELS > 1):
        for i in np.arange(2, (NUM_SIMS+1)):
            print "\n######################## START: Specie:",specie," | Gen:",i, "#####################"
            temp_top = seed_kats
            seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kats, grid, (i-1), multi_cat=True)
            if fit_score < top_kats[-1]:
                seed_kats = temp_top
                top_kats.append(top_kats[-1])
            else:
                top_kats.append(fit_score)
            avg_kats.append(avg_fitness)
            playback(vis, play,copy.deepcopy(seed_kats),i)
            print "######################## END: Specie:",specie," | Gen:",i, "#######################\n"
    #vis.graph(top_kats)
    return copy.deepcopy(list(top_kats))


progenitor = Kat(0,0)
grid = hunger_grid()
vis = Visualizer(grid)

start_time = time.time()

for i in range(SEPERATE_MODELS):
    grid = hunger_grid(i*.01)
    full_graph[i] = model(progenitor, vis, grid, i)
    full_graph_bk[i] = [grid.lava_chance, grid.berry_chance]

tki_breakdown /= SEPERATE_MODELS
vis.graph(full_graph, full_graph_bk)
vis.ins_graph(tki_breakdown)
#print tki_breakdown[:]
print("--- TIME TO COMPLETE MODEL: %s seconds ---" % (time.time() - start_time))