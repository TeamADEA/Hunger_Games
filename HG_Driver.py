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

#RUN_MODEL (start_lava_%, end_lava_%, start_berry_%, end_berry_%, t_name = title)
mo.run_model()
#mo.run_model(.02,.1,t_name='Increase Lava')
#mo.run_model(.02,.02,.05,.2,'Increase Berries')
#mo.run_model(.02,.1,.1,.05, 'Lava Up, Berry Down')

