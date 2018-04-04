#! /usr/bin/env python

"""
C_component 3/10/2018 (Batchelor)
A simple example of an IPS component wrapper which has no dependencies other than the IPS
framework.  It launches a simple "physics" code, integrator.py, which in a real application  
would typically be a massively parallel code, which likely was written as a stand-alone 
with no thought of coupling to other codes.  The philosopy of the IPS is to not
require any modification of the "physics" code's usual I/O.  The role of the component
wrapper is to:
1)  Read the template input files and state input files. Update the standard code input files
    to reflect data evolution as the simulation progresses.
2)  Run the code  
3)  Read the code output files, and update "state" files which contain information common
    to multiple components

"""
import sys
import os
import subprocess
import simple_assignment_file_edit as edit
from component import Component

class C_component (Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print 'Created %s' % (self.__class__)

# ------------------------------------------------------------------------------
#
# init function
#
# Does any tasks to get needed data into the component input files and the elements
# of the state files that this component is responsible for, as of the beginning 
# of the simulation. 
#
# ------------------------------------------------------------------------------

    def init(self, timeStamp=0):
        print 'C_component.init() called'

        if (self.services == None) :
            message = 'Error in C_component init (): No self.services'
            print message
            services.error(message)
            raise
        services = self.services

    # Get global configuration parameters
        cur_state_file = self.get_config_param(services,'CURRENT_STATE')

    # Get component-specific configuration parameters. Note: Not all of these are
    # used in 'init' but if any are missing we get an exception now instead of
    # later
        BIN_PATH = self.get_component_param(services, 'BIN_PATH')
        RESTART_FILES = self.get_component_param(services, 'RESTART_FILES')
        NPROC = self.get_component_param(services, 'NPROC')
        EXECUTABLE = self.get_component_param(services, 'EXECUTABLE')

    # Copy plasma state files over to working directory
        try:
          services.stage_plasma_state()
        except Exception, e:
          print 'Error in call to stage_plasma_state()' , e
          services.error('Error in call to stage_plasma_state()')
          raise
      
    # Get input files  
        try:
          services.stage_input_files(self.INPUT_FILES)
        except Exception, e:
          print 'Error in call to stageInputFiles()' , e
          self.services.error('Error in call to stageInputFiles()')
          raise

    # Modify data in template input file with data from config file
        # None required for this example

    # Run integrator - Not needed during init for this example
        
    # Add initial data to state file
        # None required for this example

# Update plasma state files in plasma_state work directory
        try:
          services.update_plasma_state()
        except Exception:
          message = 'Error in call to update_plasma_state()'
          print message
          services.error(message)
          raise

# "Archive" output files in history directory

        try:
          services.stage_output_files(timeStamp, self.OUTPUT_FILES)
        except Exception:
          message = 'Error in call to stage_output_files()'
          print message
          services.error(message)
          raise

        return

# ------------------------------------------------------------------------------
#
# RESTART function
# Gets restart files from restart directory
# Loads the global configuration parameters from the config file
#
# ------------------------------------------------------------------------------
        
    def restart(self, timeStamp):
        print 'C_component.restart() called'

        if (self.services == None) :
            message = 'Error in C_component init(): No self.services'
            print message
            services.error(message)
            raise
        services = self.services
        workdir = services.get_working_dir()

        # Get restart files listed in config file.        
        restart_root = self.get_config_param(services,'RESTART_ROOT')
        restart_time = self.get_config_param(services,'RESTART_TIME')

        try:
            services.get_restart_files(restart_root, restart_time, self.RESTART_FILES)
        except Exception:
            message = 'Error in call to get_restart_files()'
            print message
            self.services.error(message)
            raise
        return 0

# ------------------------------------------------------------------------------
#
# STEP function
#
# Runs the "physics code"  integrator.py
#
# ------------------------------------------------------------------------------

    def step(self, timeStamp):
        print 'C_component.step() called'

        if (self.services == None) :
            message = 'Error in C_component init (): No self.services'
            print message
            services.error(message)
            raise
        services = self.services

    # Get global configuration parameters
        cur_state_file = self.get_config_param(services,'CURRENT_STATE')
 
    # Get component-specific configuration parameters.
        BIN_PATH = self.get_component_param(services, 'BIN_PATH')
        RESTART_FILES = self.get_component_param(services, 'RESTART_FILES')
        NPROC = self.get_component_param(services, 'NPROC')
        EXECUTABLE = self.get_component_param(services, 'EXECUTABLE')

    # Copy plasma state files over to working directory
        try:
          services.stage_plasma_state()
        except Exception, e:
          print 'Error in call to stage_plasma_state()' , e
          services.error('Error in call to stage_plasma_state()')
          raise
      
    # Get input files  
        try:
          services.stage_input_files(self.INPUT_FILES)
        except Exception:
          print 'Error in call to stageInputFiles()'
          self.services.error('Error in call to stageInputFiles()')
          raise

    # Modify data in template input file with data from config file
        # no data to modify for this example.
        
    # Modify data in template input file with data from state files
        # Get data from cur_state_file
        state_dict = edit.input_file_to_variable_dict(cur_state_file)
        change_dict = {'X':state_dict['X'], 'Y':state_dict['Y']}
        delta_t = float(state_dict['t1']) - float(state_dict['t0'])
        change_dict['delta_t'] = delta_t

        # Get data from X_dot_code.out
        state_dict = edit.input_file_to_variable_dict('X_dot_code.out')
        change_dict['X_dot'] = state_dict['X_dot']

        # Get data from X_dot_code.out
        state_dict = edit.input_file_to_variable_dict('Y_dot_code.out')
        change_dict['Y_dot'] = state_dict['Y_dot']

        # Put data in integrator input fule
        edit.modify_variables_in_file(change_dict, 'integrator.in')
      
    # Run integrator with modified template input file
        cmd = [EXECUTABLE]
        print 'Executing = ', cmd
        services.send_portal_event(event_type = 'COMPONENT_EVENT',\
          event_comment =  cmd)
        retcode = subprocess.call(cmd)
        if (retcode != 0):
            logMsg = 'Error executing '.join(map(str, cmd))
            self.services.error(logMsg)
            raise Exception(logMsg)

# Update state files from C_code output
        variable_dict = edit.input_file_to_variable_dict('integrator.out')
        change_dict = {'X':variable_dict['X'], 'Y':variable_dict['Y']}
        edit.modify_variables_in_file(change_dict, cur_state_file)
        services.update_plasma_state()
        print (' ')

# "Archive" output files in history directory
        try:
            services.stage_output_files(timeStamp, self.OUTPUT_FILES)
        except Exception:
            message = 'Error in call to stage_output_files()'
            print message
            services.error(message)
            raise

        return

# ------------------------------------------------------------------------------
#
# checkpoint function
# Saves plasma state files to restart directory
#
# ------------------------------------------------------------------------------

    def checkpoint(self, timestamp=0.0):
        print 'C_component.checkpoint() called'
        if (self.services == None) :
            message = 'Error in C_component init (): No self.services'
            print message
            services.error(message)
            raise
        services = self.services
        services.save_restart_files(timestamp, self.RESTART_FILES)
        return 0

# ------------------------------------------------------------------------------
#
# finalize function
#
# Does nothing
# ------------------------------------------------------------------------------



    def finalize(self, timestamp=0.0):
        print 'C_component finalize() called'

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
        except Exception :
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
