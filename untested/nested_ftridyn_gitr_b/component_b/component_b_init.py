#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for COMPONENT B Init component.
#
#-------------------------------------------------------------------------------

from component import Component
import zipfile

#-------------------------------------------------------------------------------
#
#  COMPONENT B Init Class
#
#-------------------------------------------------------------------------------
class component_b_init(Component):
    
#-------------------------------------------------------------------------------
#
#  COMPONENT B Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('component_b_init: Construct')
        Component.__init__(self, services, config)

#-------------------------------------------------------------------------------
#
#  component_b_init Component init method. This method prepairs the input files.
#  This allows staging the plasma state files and creates the inital state.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('component_b_init: init')
    
#  Stage input files.
        self.services.stage_input_files(self.INPUT_FILES)

#  Create plasma state from files.
        zip_ref = zipfile.ZipFile(self.services.get_config_param('CURRENT_COMPONENT_B_STATE'), 'a')
        zip_ref.write(self.services.get_config_param('COMPONENT_B_NAMELIST_INPUT'))
        zip_ref.close()

#  Update the plasma state.
        self.services.update_plasma_state()

#-------------------------------------------------------------------------------
#
#  component_b_init Component step method. This component does nothing and is
#  never called.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('component_b_init: step')

#-------------------------------------------------------------------------------
#
#  component_b_init Component finalize method. This cleans up afterwards. Not
#  used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('component_b_init: finalize')
