#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS driver for massive_serial_subworkflow component.
#
#-------------------------------------------------------------------------------

from ipsframework import Component
import os
import shutil
from ips_component_utilities import ZipState
from configobj import ConfigObj

#-------------------------------------------------------------------------------
#
#  Driver Component
#
#-------------------------------------------------------------------------------
class massive_serial_subworkflow(Component):

#-------------------------------------------------------------------------------
#
#  Driver Component constructor
#
#-------------------------------------------------------------------------------
    def __init_(self, services, config):
        Component.__init_(self, services, config)

#-------------------------------------------------------------------------------
#
#  Driver Component init method
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):

        self.services.stage_input_files(self.INPUT_FILES)

#  Keys for the subworkflow.
        keys = {
            'PWD'            : self.services.get_config_param('PWD'),
            'SIM_NAME'       : 'Example_massive_serial_subworkflow',
            'LOG_FILE'       : 'log.Example_massive_serial_subworkflow',
            'NNODES'         : 1,
            'INPUT_DIR_SIM'  : 'massive_serial_subworkflow_input_dir',
            'OUTPUT_DIR_SIM' : '{}/massive_serial_subworkflow_output_dir'.format(os.getcwd())
        }

        if os.path.exists('massive_serial_subworkflow_input_dir'):
            shutil.rmtree('massive_serial_subworkflow_input_dir')
        os.mkdir('massive_serial_subworkflow_input_dir')

        massive_serial_config = self.services.get_config_param('MASSIVE_SERIAL_CONFIG')
        massive_serial_node_config = self.services.get_config_param('MASSIVE_SERIAL_NODE_CONFIG')
        fastran_config = self.services.get_config_param('FASTRAN_CONFIG')

        self.massive_serial_worker = {
            'sim_name' : None,
            'init'     : None,
            'driver'   : None
        }

        (self.massive_serial_worker['sim_name'],
         self.massive_serial_worker['init'],
         self.massive_serial_worker['driver']) = self.services.create_sub_workflow('massive_serial',
                                                                                   massive_serial_config,
                                                                                   keys,
                                                                                   'massive_serial_subworkflow_input_dir')

        massive_serial_state = self.services.get_config_param('MASSIVE_SERIAL_STATE')

        shutil.copy2(massive_serial_state, 'massive_serial_subworkflow_input_dir')
        os.chdir('massive_serial_subworkflow_input_dir')

        with ZipState.ZipState(massive_serial_state, 'r') as zip_ref:
            zip_ref.extractall()
            with ZipState.ZipState('input.zip', 'r') as input_ref:
               input_ref.extractall()


        override = ConfigObj(infile=massive_serial_node_config, interpolation='template', file_error=True)
        override['INPUT_DIR_SIM'] = os.getcwd()
        override.write()

        override2 = ConfigObj(infile=fastran_config, interpolation='template', file_error=True)
        override2['INPUT_DIR_SIM'] = os.getcwd()
        override2.write()

        os.chdir('../')

        self.wait = self.services.call_nonblocking(self.massive_serial_worker['init'], 'init', timeStamp)

#-------------------------------------------------------------------------------
#
#  Driver Component step method
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        self.services.wait_call(self.wait, True)

        self.services.call(self.massive_serial_worker['driver'], 'init', timeStamp)
        self.services.call(self.massive_serial_worker['driver'], 'step', timeStamp)

        self.services.stage_subflow_output_files()
