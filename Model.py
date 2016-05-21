from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *


top_kats = []
NUM_SIMS = 3
STEPS_PER_SIM = 300

def one_sim(seedKat):
    sim_temp = sim_manager(seedKat)
    
    for i in range(STEPS_PER_SIM):
        sim_temp.update()
    kat_temp, score_temp = sim_temp.top_kat()
    return kat_temp, score_temp

def model(seed_kat):
    for i in range(NUM_SIMS):
        seed_kat, fit_score = one_sim(seed_kat)
        top_kats.append(fit_score)


progenitor = Kat(0,0)

fit_kat, fit_score = one_sim(progenitor)
top_kats.append(fit_score)  

model(fit_kat)
print top_kats
        
