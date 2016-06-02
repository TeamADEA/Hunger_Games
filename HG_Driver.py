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


#mo.run_model(from_lava = .02,       # START LAVA CHANCE
                # to_lava = .02,     # END FROM LAVA CHANCE
                # from_berry = .05,  # START BERRY CHANCE
                # to_berry = .05,    # END BERRY CHANCE
                # from_mut=10,       # START MUTATION CHANCE
                # to_mut=10,         # END MUTATION CHANCE
                # from_gen = 33,     # START GENERATE CHANCE
                # to_gen = 33,       # END GENERATE CHANCE
                #t_name = 'Default'  # TITLE OF TEST
                # frames = -1        # Defaults to -1 (-1:Don't, 0:Only Last, N:every N)

#mo.run_model() #Default
mo.run_model(.02,.5,.05,.05, 10, 10, 33, 33, 'Lava World')
mo.run_model(.2,.2,.05,.01, 10, 50, 33, 33, 'Nuclear Wasteland', 0)
#mo.run_model(.02,.5,.05,.5, 10, 10, 33, 33, 'Berry World')
mo.run_model(.00,.00,.1,.1, 10, 10, 33, 33, "No Lava")
#mo.run_model(.1,.1,0.0,0.0, 10, 10, 33, 33, "No Berries")
#mo.run_model(.1,.1,.1,.1,10,10,33,33,"Lava & Berries")





