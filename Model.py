from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
import Hunger_Grid as hg

top_kats = []
NUM_SIMS = 300
STEPS_PER_SIM = 300


def one_sim(seedKat):
    """Run one simulation of number of time steps (default: 300)
        
    First initialize a sim_manager with first Kat agent.
	Then update at each time steps, finally taking the top
	Kat and top fitness score, returns it.
    """
    sim_temp = sim_manager(seedKat)
    
    for i in range(STEPS_PER_SIM):
        sim_temp.update()
    
    kat_temp, score_temp = sim_temp.top_kat()
    return kat_temp, score_temp, sim_temp.return_playback()

def playback(vis, pb):
    vis.show(pb[0])

def model(seed_kat, vis):
    """Run multiple simulation of number of time steps each,
	(default: 300 simulations).
        
    In a loop, keep running each simulation of 300 
	number of time steps, append the top fitness score,
	and after loops ended, graph the fitness score over
	generations (simulations).
    """
    for i in range(NUM_SIMS):
        seed_kat, fit_score, play = one_sim(seed_kat)
        top_kats.append(fit_score)
        playback(vis, play)
    vis.graph(top_kats)

progenitor = Kat(0,0)
vis = Visualizer(hg.createHungerGrid())

fit_kat, fit_score, play = one_sim(progenitor)
top_kats.append(fit_score)  
playback(vis, play)

model(fit_kat, vis)
print top_kats
        
