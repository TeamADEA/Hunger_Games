from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
import Hunger_Grid as hg

top_kats = []
NUM_SIMS = 300
STEPS_PER_SIM = 300


def one_sim(seedKat):
    sim_temp = sim_manager(seedKat)
    
    for i in range(STEPS_PER_SIM):
        sim_temp.update()
    
    kat_temp, score_temp = sim_temp.top_kat()
    return kat_temp, score_temp, sim_temp.return_playback()

def playback(vis, pb):
    vis.show(pb[0])

def model(seed_kat, vis):
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
        
