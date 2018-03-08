
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for COMPONENT B Driver component.
#
#-------------------------------------------------------------------------------

from component import Component

#-------------------------------------------------------------------------------
#
#  COMPONENT B Driver Class
#
#-------------------------------------------------------------------------------
class component_b_driver(Component):

#-------------------------------------------------------------------------------
#
#  component_b_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('component_b_driver: Construct')
        Component.__init__(self, services, config)
        self.running_components = {}
    
#-------------------------------------------------------------------------------
#
#  component_b_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('component_b_driver: init')

#  Get the ports for the various components.
        self.component_b_port = self.services.get_port('COMPONENT_B')
    
#  Initialize the component for the first time. Not sure if this is necessary or
#  if I can just pass **keywords to the next component.
        if 'override' in keywords:
            self.running_components['component_b:init'] = self.services.call_nonblocking(self.component_b_port,
                                                                                         'init',
                                                                                         timeStamp,
                                                                                         namelist_override = keywords['override'])
        else:
            self.running_components['component_b:init'] = self.services.call_nonblocking(self.component_b_port,
                                                                                         'init',
                                                                                         timeStamp)

#-------------------------------------------------------------------------------
#
#  component_b_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('component_b_driver: step')

#  Wait until all the dependent components are finished.
        self.services.wait_call_list([self.running_components['component_b:init']], True)
        self.running_components['component_b:step'] = self.services.call_nonblocking(self.component_b_port,
                                                                                     'step',
                                                                                     timeStamp)
#  Clear the waiting condition since we are no longer waiting for the init
#  method of component_b to run.
        del self.running_components['component_b:init']

#-------------------------------------------------------------------------------
#
#  component_b_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('component_b_driver: finalize')
        
#  Call finalize on all components. The INIT component automatically calls the
#  finalize method.
        self.running_components['component_b:finalize'] = self.services.call_nonblocking(self.component_b_port,
                                                                                         'finalize',
                                                                                         timeStamp)
        
#  Wait until all the components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
