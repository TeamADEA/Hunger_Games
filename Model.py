import numpy as np
import copy
from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
from Hunger_Grid import hunger_grid

top_kats = []
avg_kats = []


STEP_SIZE = 30 # 0 = only last frame,

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

def playback(vis, pb, best_kat, gen):
    if (STEP_SIZE == -1):
        return
    if (STEP_SIZE == 0):
        vis.show(pb[-1], best_kat, gen)
    else:
        for i in np.arange(0,len(pb), STEP_SIZE):
            vis.show(pb[i], best_kat, gen)


def model(seed_kat, vis, grid):
    """Run multiple simulation of number of time steps each,
	(default: 300 simulations).

    In a loop, keep running each simulation of 300
	number of time steps, append the top fitness score,
	and after loops ended, graph the fitness score over
	generations (simulations).
    """
    print "Gen:1"
    seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kat, grid)
    top_kats.append(fit_score)
    avg_kats.append(avg_fitness)
    playback(vis, play, seed_kat, 1)
    for i in np.arange(2, NUM_SIMS):
        print "Gen:", i
        temp_top = seed_kats
        seed_kat, fit_score, play, avg_fitness, seed_kats = one_sim(seed_kats, grid, multi_cat=True)
        if fit_score < top_kats[-1]:
            seed_kats = temp_top
            top_kats.append(top_kats[-1])
            #avg_kats.append(avg_kats[-1])
        else:
            top_kats.append(fit_score)
        avg_kats.append(avg_fitness)
        playback(vis, play,seed_kat,i)
    vis.graph(top_kats)


progenitor = Kat(0,0)
grid = hunger_grid()
vis = Visualizer(grid)
model(progenitor, vis, grid)
