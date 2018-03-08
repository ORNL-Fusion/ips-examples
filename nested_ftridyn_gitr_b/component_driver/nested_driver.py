
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for NESTED Driver component.
#
#-------------------------------------------------------------------------------

from component import Component
import os
import shutil

#-------------------------------------------------------------------------------
#
#  NESTED Driver Class
#
#-------------------------------------------------------------------------------
class nested_driver(Component):

#-------------------------------------------------------------------------------
#
#  nested_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('nested_driver: Construct')
        Component.__init__(self, services, config)
        self.async_queue = {}
    
#-------------------------------------------------------------------------------
#
#  nested_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('nested_driver: init')

        self.nested_components = {}
    
#  Sub workflows require manual setup. First a sub directory must be created.
#  Then copying of the input files must be performed manually. The first
#  argument of create sub workflow doesn't appear to do anything.
        self.services.stage_input_files(self.INPUT_FILES)
        
        self.nested_components['component_a'] = {'sim_name': None, 'init': None, 'driver': None, 'sub_working_dir': 'component_a_init'}
        print(self.nested_components['component_a'])
        print(self.nested_components['component_a']['sub_working_dir'])
 
        os.mkdir(self.nested_components['component_a']['sub_working_dir'])
        shutil.copy2(self.services.get_config_param('COMPONENT_A_NAMELIST_INPUT'), self.nested_components['component_a']['sub_working_dir'])
        (self.nested_components['component_a']['sim_name'],
         self.nested_components['component_a']['init'],
         self.nested_components['component_a']['driver']) = self.services.create_sub_workflow('component_a_sub',self.services.get_config_param('COMPONENT_A_CONF'),
        {
        
        'PWD' : self.services.get_config_param('PWD'),
        'COMPONENT_A_NAMELIST_INPUT' : self.services.get_config_param('COMPONENT_A_NAMELIST_INPUT'),
        'LOG_FILE' : 'log.component_a.warning'
        })
                                                                                              
        self.nested_components['component_b'] = {'sim_name': None, 'init': None, 'driver': None, 'sub_working_dir': 'component_b_init'}
        os.mkdir(self.nested_components['component_b']['sub_working_dir'])
        shutil.copy2(self.services.get_config_param('COMPONENT_B_NAMELIST_INPUT'), self.nested_components['component_b']['sub_working_dir'])
        (self.nested_components['component_b']['sim_name'],
         self.nested_components['component_b']['init'],
         self.nested_components['component_b']['driver']) = self.services.create_sub_workflow('component_b_sub',
                                                                                              self.services.get_config_param('COMPONENT_B_CONF'),
                                                                                              {
                                                                                              'PWD'                        : self.services.get_config_param('PWD'),
                                                                                              'COMPONENT_B_NAMELIST_INPUT' : self.services.get_config_param('COMPONENT_B_NAMELIST_INPUT'),
                                                                                              'LOG_FILE'                   : 'log.component_b.warning'
                                                                                              })

#  Inialized the plasma state by calling the init components of the sub
#  workflows.
        #self.async_queue['component_a:init:init'] = self.services.call_nonblocking(self.nested_components['component_a']['init'], 'init', timeStamp)
        self.async_queue['component_b:init:init'] = self.services.call_nonblocking(self.nested_components['component_b']['init'], 'init', timeStamp)
    
#  Initalize the sub workflow drivers. We want to pass arguments to the sub
#  workflow components. Create a dictionary of dictionaries for the stuff to
#  override. Need some standard naming convection here.
        #self.services.wait_call_list([self.async_queue['component_a:init:init']], True)
        self.async_queue['component_a:driver:init'] = self.services.call_nonblocking(self.nested_components['component_a']['driver'], 'init', timeStamp)
                                                                                     #override = {'message': 'called from nested'})
        #del self.async_queue['component_a:init:init']

        self.services.wait_call_list([self.async_queue['component_b:init:init']], True)
        self.async_queue['component_b:driver:init'] = self.services.call_nonblocking(self.nested_components['component_b']['driver'], 'init', timeStamp,
                                                                                     override = {'message': 'called from nested'})
        del self.async_queue['component_b:init:init']
    
#-------------------------------------------------------------------------------
#
#  nested_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('nested_driver: step')

#  Step the drivers. Here Component a doesn't depend on component b so both can
#  be run in parallel.
        self.services.wait_call_list([self.async_queue['component_a:driver:init']], True)
        self.async_queue['component_a:driver:step'] = self.services.call_nonblocking(self.nested_components['component_a']['driver'], 'step', 0.0)
        del self.async_queue['component_a:driver:init']
        
        self.services.wait_call_list([self.async_queue['component_b:driver:init']], True)
        self.async_queue['component_b:driver:step'] = self.services.call_nonblocking(self.nested_components['component_b']['driver'], 'step', 0.0)
        del self.async_queue['component_b:driver:init']
    
#-------------------------------------------------------------------------------
#
#  nested_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('nested_driver: finalize')

#  Wait until everything is finished before finalizing.
        self.services.wait_call_list(self.async_queue.values(), True)
        self.async_queue = {}

#  Call the finalize methods.
        #self.async_queue['component_a:init:finalize'] = self.services.call_nonblocking(self.nested_components['component_a']['init'], 'finalize', timeStamp)
        self.async_queue['component_b:init:finalize'] = self.services.call_nonblocking(self.nested_components['component_b']['init'], 'finalize', timeStamp)
        self.async_queue['component_a:driver:finalize'] = self.services.call_nonblocking(self.nested_components['component_a']['driver'], 'finalize', timeStamp)
        self.async_queue['component_b:driver:finalize'] = self.services.call_nonblocking(self.nested_components['component_b']['driver'], 'finalize', timeStamp)

#  Wait until everything is finished before finalizing.
        self.services.wait_call_list(self.async_queue.values(), True)
        self.async_queue = {}
