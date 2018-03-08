#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for COMPONENT B component.
#
#-------------------------------------------------------------------------------

from component import Component
import zipfile

#-------------------------------------------------------------------------------
#
#  COMPONENT B Class
#
#-------------------------------------------------------------------------------
class component_b(Component):
    
#-------------------------------------------------------------------------------
#
#  COMPONENT B Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('component_b: Construct')
        Component.__init__(self, services, config)
        self.running_tasks = {}

#-------------------------------------------------------------------------------
#
#  component_b Component init method. This method prepairs the input files.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('component_b: init')

#  Stage plasma state.
        self.services.stage_plasma_state()
        
#  Unzip files from the plasma state. Use mode a so files can be read and
#  written to.
        self.zip_ref = zipfile.ZipFile(self.services.get_config_param('CURRENT_COMPONENT_B_STATE'), 'a')
        self.zip_ref.extract(self.services.get_config_param('COMPONENT_B_NAMELIST_INPUT'))

#  Arguments can be passed in from the config file. All definitions from the
#  config file come in as a string.
#  FIXME: Make this a dictionary.
        self.component_b_args = [ self.COMPONENT_B_ARGS ]

#  keywords allow passing arguments from the calling component. keywords may not
#  exist so check for them fits.
        if 'COMPONENT_B_ARGS' in keywords:
            self.component_b_args.extend(keywords['COMPONENT_B_ARGS'])

#  Extract an extry from the component d namelist input file.
        
        #  Override the values in the namelist input file.
        #if 'namelist_override' in keywords:
        #    for key, value in keywords['namelist_override'].iteritems():
                #namelist_example_file['component_b_nl'][key] = value
        
        #self.component_b_args.extend([''.join(namelist_example_file['component_b_nl']['message'])])

#-------------------------------------------------------------------------------
#
#  component_b Component step method. This runs code the component is wrapped
#  around.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0, **keywords):
        print('component_b: step')

#  keywords allow passing arguments from the calling component. keywords may not
#  exist so check for them fits.
#  FIXME: Make this a dictionary.
        if 'COMPONENT_B_ARGS' in keywords:
            self.component_b_args.extend(keywords['COMPONENT_B_ARGS'])
    
#  Launch a task. Task launches are non blocking so save the task id. Depending
#  on the system, install locations and binary names can be different. Note, I'm
#  using the log file as an output since it pipes output there.
        self.running_tasks['task1'] = self.services.launch_task(self.NPROC,
                                                                self.services.get_working_dir(),
                                                                self.COMPONENT_B_EXE,
                                                                *self.component_b_args,
                                                                logfile = self.services.get_config_param('COMPONENT_B_OUTPUT'))

#  Wait for the task to complete.
        self.services.wait_task(self.running_tasks['task1'])
        del self.running_tasks['task1']

#  Update the plasma state.
        self.zip_ref.write(self.services.get_config_param('COMPONENT_B_OUTPUT'))
        self.zip_ref.close()
            
        self.services.update_plasma_state()
    
#-------------------------------------------------------------------------------
#
#  component_b Component finalize method. This cleans up afterwards. Not used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('component_b: finalize')
        for value in self.running_tasks:
            self.services.wait_task(value)

