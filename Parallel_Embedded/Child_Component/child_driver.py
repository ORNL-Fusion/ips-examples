
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for CHILD Driver component.
#
#-------------------------------------------------------------------------------

from component import Component

#-------------------------------------------------------------------------------
#
#  CHILD Driver Class
#
#-------------------------------------------------------------------------------
class child_driver(Component):

#-------------------------------------------------------------------------------
#
#  child_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('child_driver: Construct')
        Component.__init__(self, services, config)
        self.running_components = {}
        self.ports = {}

#-------------------------------------------------------------------------------
#
#  child_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('child_driver: init')

#  Get the ports for the various components.
        self.ports['CHILD'] = self.services.get_port('CHILD')

#  Initialize the component for the first time.
        self.running_components['child:init'] = self.services.call_nonblocking(self.ports['CHILD'],
                                                                               'init', timeStamp,
                                                                               **keywords)

#-------------------------------------------------------------------------------
#
#  child_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('child_driver: step')

#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}
        self.running_components['child:step'] = self.services.call_nonblocking(self.ports['CHILD'],
                                                                               'step', timeStamp)

#  The child component step was calling with a non blocking call. If we want
#  callers of this components step method to wait, we need to block until the
#  child component step is finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}

#-------------------------------------------------------------------------------
#
#  child_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('child_driver: finalize')
        
#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}
        
#  Call finalize on all components. The INIT component automatically calls the
#  finalize method.
        self.running_components['child:finalize'] = self.services.call_nonblocking(self.ports['CHILD'],
                                                                                   'finalize', timeStamp)

#  Wait until all the components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
