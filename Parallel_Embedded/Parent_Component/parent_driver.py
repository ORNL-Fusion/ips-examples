
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for PARENT Driver component.
#
#-------------------------------------------------------------------------------

from component import Component
import os

#-------------------------------------------------------------------------------
#
#  PARENT Driver Class
#
#-------------------------------------------------------------------------------
class parent_driver(Component):

#-------------------------------------------------------------------------------
#
#  parent_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('parent_driver: Construct')
        Component.__init__(self, services, config)
        self.running_components = {}
        self.child_components = {}
    
#-------------------------------------------------------------------------------
#
#  parent_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('parent_driver: init')
    
        num_children = int(self.services.get_config_param('NUM_CHILDREN'))
        child_conf = self.services.get_config_param('CHILD_COMPONENT_CONF')
        
        keys = {
               'PWD' : self.services.get_config_param('PWD')
               }
        
        for i in range(0, num_children):
            child_comp = 'child_{}'.format(i)
            
            keys['LOG_FILE'] = 'log.{}'.format(child_comp)
            keys['SIM_NAME'] = child_comp
            
            self.child_components[child_comp] = {
                                                'sim_name'  : None,
                                                'init'      : None,
                                                'driver'    : None,
                                                'input_dir' : '{}_dir'.format(child_comp)
                                                }
#  Input files will be staged from this directory.
            os.mkdir(self.child_components[child_comp]['input_dir'])
            #  Copy files to the created directory.
            (self.child_components[child_comp]['sim_name'],
             self.child_components[child_comp]['init'],
             self.child_components[child_comp]['driver']) = self.services.create_sub_workflow(child_comp,
                                                                                              child_conf,
                                                                                              keys,
                                                                                              self.child_components[child_comp]['input_dir'])

#  Loop over the children and all the initize component.
        for child in self.child_components.values():
            self.running_components['{}:init:init'.format(child['sim_name'])] = self.services.call_nonblocking(child['init'],
                                                                                                               'init', timeStamp)
            
#  Loop over the children and all the initize component.
        for child in self.child_components.values():
            keys = {'message' : 'Hello from {}'.format(child['sim_name'])}
            self.services.wait_call(self.running_components['{}:init:init'.format(child['sim_name'])], True)
            self.running_components['{}:driver:init'.format(child['sim_name'])] = self.services.call_nonblocking(child['driver'],
                                                                                                                 'init', timeStamp,
                                                                                                                 **keys)
            del self.running_components['{}:init:init'.format(child['sim_name'])]
            
#-------------------------------------------------------------------------------
#
#  parent_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('parent_driver: step')
        
#  Loop over the children and all the initize component.
        for child in self.child_components.values():
            self.services.wait_call(self.running_components['{}:driver:init'.format(child['sim_name'])], True)
            self.running_components['{}:driver:step'.format(child['sim_name'])] = self.services.call_nonblocking(child['driver'],
                                                                                                                 'step', timeStamp)
            del self.running_components['{}:driver:init'.format(child['sim_name'])]
    
#-------------------------------------------------------------------------------
#
#  parent_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('parent_driver: finalize')

#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}

#  Call finalize on all components. Need to manually call finalize on init components.
        for child in self.child_components.values():
            self.running_components['{}:init:finalize'.format(child['sim_name'])] = self.services.call_nonblocking(child['init'],
                                                                                                                   'finalize', timeStamp)
            self.running_components['{}:driver:finalize'.format(child['sim_name'])] = self.services.call_nonblocking(child['driver'],
                                                                                                                     'finalize', timeStamp)

#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
