import numpy as np
import copy
from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
import Hunger_Grid as hg
import Mutate as m

grid  = hg.createHungerGrid(20,20)
my_kat = Kat(10,10)
my_kat.generate_behavior(grid)
my_kat.generate_behavior(grid)
my_kat.generate_behavior(grid)
my_kat.generate_behavior(grid)
my_kat.generate_behavior(grid)
my_kat.print_ins_1()
m.mutate_kat(my_kat,.8)
my_kat.print_ins_1()

