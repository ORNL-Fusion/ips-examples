#! /usr/bin/env python

"""
basic_init.py  Batchelor (3-11-2018)

Version 1.0 (Batchelor 3/11/2018)
Simplified initializer adapted from generic_ps_init.py, but eliminating reference to many
features specific to plasma physics.  The immediate application is to simple, example
simulations which do not make use of the SWIM Plasma State system.  The IPS framework uses
the terminology plasma state to refer to all state files.  But the SWIM Plasma State need
not be used at all.

By default this script merely touches all the files listed as PLASMA_STATE_FILES in the 
config file.  If a CURRENT_STATE is specified in the simulation config file, this script
adds the run_id and time loop variables to it -> tinit, and tfinal 

If more work needs to be done before the individual components do 
their own init, one can specify an INIT_HELPER_CODE (full path) in the config file
which if present will be executed here.  If input files are needed for the helper code
they must also be specified in the [init] section of the config file.

"""
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

import sys
import os
import subprocess
import shutil
import simple_assignment_file_edit as edit
from  component import Component

class basic_init (Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print 'Created %s' % (self.__class__)

# ------------------------------------------------------------------------------
#
# init function
#
# Does nothing.
#
# ------------------------------------------------------------------------------

    def init(self, timestamp=0.0):
        print (' ')
        print ('basic_init.init() called')
        return

# ------------------------------------------------------------------------------
#
# step function
#
# Calls fortran executable init_empty_plasma_state and updates plasma state
#
# ------------------------------------------------------------------------------

    def step(self, timeStamp):
        print (' ')
        print ('basic_init.step() called')

        services = self.services

# Check if this is a restart simulation
        simulation_mode = self.get_config_param(services, 'SIMULATION_MODE')

        if simulation_mode == 'RESTART':
            print 'basic_init: RESTART'
        if simulation_mode not in ['RESTART', 'NORMAL']:
            logMsg = 'basic_init: unrecoginzed SIMULATION_MODE: ' + mode
            self.services.error(logMsg)
            raise ValueError(logMsg)
 
# ------------------------------------------------------------------------------
#
# RESTART simulation mode
#
# ------------------------------------------------------------------------------
            
        if simulation_mode == 'RESTART':
            # Get restart files listed in config file. Here just the plasma state files.
            restart_root = self.get_config_param(services, 'RESTART_ROOT')
            restart_time = self.get_config_param(services, 'RESTART_TIME')
            try:
                 services.get_restart_files(restart_root, restart_time, self.RESTART_FILES)
            except:
                logMsg = 'Error in call to get_restart_files()'
                self.services.exception(logMsg)
                raise
            
            cur_state_file = self.services.get_config_param('CURRENT_STATE')
    
        # Check if there is a config parameter CURRENT_STATE and add data
            cur_state_file = self.get_config_param(services, 'CURRENT_STATE', optional = True)
            if cur_state_file != None or len(cur_state_file) > 0:
                timeloop = services.get_time_loop()
                tfinal = timeloop[-1]

                # Put data into current state. For restart only tfinal gets changed
                variable_dict = {'tfinal' : tfinal}
                edit.add_variables_to_output_file(variable_dict, cur_state_file)
        
# ------------------------------------------------------------------------------
#
# NORMAL simulation mode
#
# ------------------------------------------------------------------------------
        
        else:

            print 'basic_init: simulation mode NORMAL'
            state_file_list = self.get_config_param(services, 'PLASMA_STATE_FILES').split(' ')

        # Generate state files as dummies so framework will have a complete set
            for file in state_file_list:
                print 'touching state file = ', file
                try:
                    subprocess.call(['touch', file])
                except Exception:
                    print 'No file ', file

            init_mode = self.get_component_param(services, 'INIT_MODE', optional = True)
            if init_mode in ['touch_only', 'TOUCH_ONLY'] :
                # Update plasma state
                try:
                    services.update_plasma_state()
                except Exception, e:
                    print 'Error in call to updatePlasmaState()', e
                    raise
                return

        # Check if there is a config parameter CURRENT_STATE and add data if so.
            cur_state_file = self.get_config_param(services, 'CURRENT_STATE', optional = True)
            if cur_state_file != None and len(cur_state_file) > 0:
                run_id = self.get_config_param(services, 'RUN_ID')

                timeloop = services.get_time_loop()
                tinit = timeloop[0]
                tfinal = timeloop[-1]

                # Put data into current state
                variable_dict = {'run_id' : run_id, 'tinit' : tinit, 'tfinal' : tfinal}
                edit.add_variables_to_output_file(variable_dict, cur_state_file)


            try:       
                services.stage_input_files(self.INPUT_FILES)
            except Exception:
                message = 'basic_init: Error in staging input files'
                print message
                services.exception(message)
                raise

            INIT_HELPER_CODE_bin = self.get_component_param(services, 'INIT_HELPER_CODE', \
            optional = True)
            
            if (INIT_HELPER_CODE_bin is not None) and (len(INIT_HELPER_CODE_bin) != 0):
                cmd = [INIT_HELPER_CODE_bin]
                print 'Executing ', cmd
                services.send_portal_event(event_type = 'COMPONENT_EVENT',\
                  event_comment =  cmd)
                retcode = subprocess.call(cmd)
                if (retcode != 0):
                    logMsg = 'Error executing '.join(map(str, cmd))
                    self.services.error(logMsg)
                    raise Exception(logMsg)


# Update plasma state
        try:
            services.update_plasma_state()
        except Exception, e:
            print 'Error in call to updatePlasmaState()', e
            raise

# "Archive" output files in history directory
        services.stage_output_files(timeStamp, self.OUTPUT_FILES)

# ------------------------------------------------------------------------------
#
# checkpoint function
#
# Saves plasma state files to restart directory
# ------------------------------------------------------------------------------

    def checkpoint(self, timestamp=0.0):
        print 'basic_init.checkpoint() called'
        
        services = self.services
        services.stage_plasma_state()
        services.save_restart_files(timestamp, self.RESTART_FILES)
        

# ------------------------------------------------------------------------------
#
# finalize function
#
# Does nothing
# ------------------------------------------------------------------------------



    def finalize(self, timestamp=0.0):
        print 'basic_init.finalize() called'

# ------------------------------------------------------------------------------
#
# "Private"  methods
#
# ------------------------------------------------------------------------------


    # Try to get config parameter - wraps the exception handling for get_config_parameter()
    def get_config_param(self, services, param_name, optional=False):

        try:
            value = services.get_config_param(param_name)
            print param_name, ' = ', value
        except Exception:
            if optional:
                print 'config parameter ', param_name, ' not found'
                value = None
            else:
                message = 'required config parameter ', param_name, ' not found'
                print message
                services.exception(message)
                raise

        return value

    # Try to get component specific config parameter - wraps the exception handling
    def get_component_param(self, services, param_name, optional=False):

        if hasattr(self, param_name):
            value = getattr(self, param_name)
            print param_name, ' = ', value
        elif optional:
            print 'optional config parameter ', param_name, ' not found'
            value = None
        else:
            message = 'required component config parameter ', param_name, ' not found'
            print message
            services.exception(message)
            raise

        return value
