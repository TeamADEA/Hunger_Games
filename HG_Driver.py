from HG_Code.HG_Test import UnitTest as UT
from HG_Code import Model as mo
from HG_Code.Visualize import Visualizer
from HG_Code.SimManager import sim_manager
from HG_Code.Hunger_Grid import hunger_grid
from HG_Code.Kat import Kat
from HG_Code import hg_settings
from HG_Code import Mutate as mu

unitTest = UT.Run_Unit_Test()
unitTest.run_test()

#mo.run_model(from_lava = .02, to_lava = .02, from_berry = .05, to_berry = .05,\
#            from_mut=10, to_mut=10, from_gen = 33, to_gen = 33,t_name = 'Default')
#mo.run_model()

#mo.run_model() #Default
mo.run_model(.02,.02,.05,.05, 10, 10, 80, 110, 'Generate Behavior Only')





