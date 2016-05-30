import numpy as np
import copy
from Kat import Kat
from Visualize import Visualizer
from SimManager import sim_manager
from hg_settings import *
import Hunger_Grid as hg
import Mutate as m

my_kat = Kat(10,10)

m.generate_behavior(my_kat, 100)
m.delete_behavior(my_kat.instruction_set_1, 2)
my_kat.print_ins_1()

m.generate_behavior(my_kat, 100)
m.delete_behavior(my_kat.instruction_set_1, 2)
my_kat.print_ins_1()

m.generate_behavior(my_kat, 100)
m.delete_behavior(my_kat.instruction_set_1, 2)
my_kat.print_ins_1()

m.generate_behavior(my_kat, 100)
m.delete_behavior(my_kat.instruction_set_1, 2)
my_kat.print_ins_1()

m.generate_behavior(my_kat, 100)
m.delete_behavior(my_kat.instruction_set_1, 2)
my_kat.print_ins_1()

