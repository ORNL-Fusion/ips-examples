#! /usr/bin/env python

"""
A_component 3/10/2018 (Batchelor)
A simple example of an IPS component wrapper which has no dependencies other than the IPS
framework.  It launches a simple "physics" code, X_dot_code.py, which in a real application  
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
from __future__ import print_function
import sys
import os
import subprocess
import utils.simple_assignment_file_edit as edit
import utils.get_IPS_config_parameters as config
from component import Component

class A_component (Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print('Created %s' % (self.__class__))

# ------------------------------------------------------------------------------
#
# init function
#
# Does any tasks to get needed data into the component input files and the elements
# of the state files that this component is responsible for, as of the beginning 
# of the simulation. For this simple example that only entails putting the initial value
# of X into the current state file.
#
# ------------------------------------------------------------------------------

    def init(self, timeStamp=0):
        print('A_component.init() called')

        if (self.services == None) :
            message = 'Error in A_component init (): No self.services'
            print(message)
            services.error(message)
            raise
        services = self.services

    # Get global configuration parameters
        cur_state_file = config.get_config_param(self, services,'CURRENT_STATE')

    # Get component-specific configuration parameters. Note: Not all of these are
    # used in 'init' but if any are missing we get an exception now instead of
    # later
        BIN_PATH = config.get_component_param(self, services, 'BIN_PATH')
        RESTART_FILES = config.get_component_param(self, services, 'RESTART_FILES')
        NPROC = config.get_component_param(self, services, 'NPROC')
        EXECUTABLE = config.get_component_param(self, services, 'EXECUTABLE')
        X0 = config.get_component_param(self, services, 'X0')
        a_lin = config.get_component_param(self, services, 'a_lin')
        b_nonlin = config.get_component_param(self, services, 'b_nonlin')

    # Copy  state files over to working directory
        try:
          services.stage_state()
        except Exception as e:
          print('Error in call to stage_state()' , e)
          services.error('Error in call to stage_state()')
          raise
      
    # Get input files  
        try:
          services.stage_input_files(self.INPUT_FILES)
        except Exception as e:
          print('Error in call to stageInputFiles()' , e)
          self.services.error('Error in call to stageInputFiles()')
          raise

    # Modify data in template input file with data from config file
        change_dict = {'a_lin':a_lin, 'b_nonlin':b_nonlin}
        edit.modify_variables_in_file(change_dict, 'X_dot_code.in')

    # Run X_dot_code - Not needed during init for this example
        
    # Add initial data to state file
        variable_dict = {'X' : X0}
        edit.add_variables_to_output_file(variable_dict, cur_state_file)

# Update  state files in state work directory
        try:
          services.update_state()
        except Exception:
          message = 'Error in call to update_state()'
          print(message)
          services.error(message)
          raise

# "Archive" output files in history directory

        try:
          services.stage_output_files(timeStamp, self.OUTPUT_FILES)
        except Exception:
          message = 'Error in call to stage_output_files()'
          print(message)
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
        print('A_component.restart() called')

        if (self.services == None) :
            message = 'Error in A_component init(): No self.services'
            print(message)
            services.error(message)
            raise
        services = self.services
        workdir = services.get_working_dir()

        # Get restart files listed in config file.        
        restart_root = config.get_config_param(self, services,'RESTART_ROOT')
        restart_time = config.get_config_param(self, services,'RESTART_TIME')

        try:
            services.get_restart_files(restart_root, restart_time, self.RESTART_FILES)
        except Exception:
            message = 'Error in call to get_restart_files()'
            print(message)
            self.services.error(message)
            raise
        return 0

# ------------------------------------------------------------------------------
#
# STEP function
#
# Runs the "physics code"  X_dot_code.py
#
# ------------------------------------------------------------------------------

    def step(self, timeStamp):
        print('A_component.step() called')

        if (self.services == None) :
            message = 'Error in A_component init (): No self.services'
            print(message)
            services.error(message)
            raise
        services = self.services

    # Get global configuration parameters
        cur_state_file = config.get_config_param(self, services,'CURRENT_STATE')
 
    # Get component-specific configuration parameters.
        BIN_PATH = config.get_component_param(self, services, 'BIN_PATH')
        RESTART_FILES = config.get_component_param(self, services, 'RESTART_FILES')
        NPROC = config.get_component_param(self, services, 'NPROC')
        EXECUTABLE = config.get_component_param(self, services, 'EXECUTABLE')
        X0 = config.get_component_param(self, services, 'X0')
        a_lin = config.get_component_param(self, services, 'a_lin')
        b_nonlin = config.get_component_param(self, services, 'b_nonlin')

    # Copy state files over to working directory
        try:
          services.stage_state()
        except Exception as e:
          print('Error in call to stage_state()' , e)
          services.error('Error in call to stage_state()')
          raise
      
    # Get input files  
        try:
          services.stage_input_files(self.INPUT_FILES)
        except Exception:
          print('Error in call to stageInputFiles()')
          self.services.error('Error in call to stageInputFiles()')
          raise

    # Modify data in template input file with data from config file
        change_dict = {'a_lin':a_lin, 'b_nonlin':b_nonlin}
        edit.modify_variables_in_file(change_dict, 'X_dot_code.in')
        
    # Modify data in template input file with data from state file
        state_dict = edit.input_file_to_variable_dict(cur_state_file)
        change_dict = {'X':state_dict['X'], 'Y':state_dict['Y']}
        edit.modify_variables_in_file(change_dict, 'X_dot_code.in')
      
    # Run X_dot_code with modified template input file
        cmd = EXECUTABLE
        print('Executing = ', cmd)
        services.send_portal_event(event_type = 'COMPONENT_EVENT',\
          event_comment =  cmd)
        cwd = services.get_working_dir()
        task_id  = services.launch_task(NPROC, cwd, cmd)
        retcode = services.wait_task(task_id)
        if (retcode != 0):
            message = 'Error executing ', cmd
            print(message)
            self.services.error(message)
            raise Exception(message)
            return 1
        print(cmd, ' finished \n')


# Update state files in state work directory
        try:
          services.update_state()
        except Exception:
          message = 'Error in call to update_state()'
          print(message)
          services.error(message)
          raise

# "Archive" output files in history directory
        try:
            services.stage_output_files(timeStamp, self.OUTPUT_FILES)
        except Exception:
            message = 'Error in call to stage_output_files()'
            print(message)
            services.error(message)
            raise

        return

# ------------------------------------------------------------------------------
#
# checkpoint function
# Saves  state files to restart directory
#
# ------------------------------------------------------------------------------

    def checkpoint(self, timestamp=0.0):
        print('A_component.checkpoint() called')
        if (self.services == None) :
            message = 'Error in A_component init (): No self.services'
            print(message)
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
        print('A_component finalize() called')
        