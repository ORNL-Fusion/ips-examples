
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for TEST Driver component.
#
#-------------------------------------------------------------------------------

from component import Component

#-------------------------------------------------------------------------------
#
#  TEST Driver Class
#
#-------------------------------------------------------------------------------
class test_componet_driver(Component):

#-------------------------------------------------------------------------------
#
#  test_componet_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('test_componet_driver: Construct')
        Component.__init__(self, services, config)
        self.running_components = {}
        self.ports = {}

#-------------------------------------------------------------------------------
#
#  test_componet_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('test_componet_driver: init')

#  Get the ports for the various components.
        self.ports['TEST'] = self.services.get_port('TEST')

#  Initialize the component for the first time.
        self.running_components['test_componet:init'] = self.services.call_nonblocking(self.ports['TEST'],
                                                                                       'init', timeStamp,
                                                                                       **keywords)

#-------------------------------------------------------------------------------
#
#  test_componet_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('test_componet_driver: step')

#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}
        self.running_components['test_componet:step'] = self.services.call_nonblocking(self.ports['TEST'],
                                                                                       'step', timeStamp)

#  The test_componet component step was calling with a non blocking call. If we
#  want callers of this components step method to wait, we need to block until
#  the test_componet component step is finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}

#-------------------------------------------------------------------------------
#
#  test_componet_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('test_componet_driver: finalize')
        
#  Wait until all the dependent components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
        self.running_components = {}
        
#  Call finalize on all components. The INIT component automatically calls the
#  finalize method.
        self.running_components['test_componet:finalize'] = self.services.call_nonblocking(self.ports['TEST'],
                                                                                           'finalize', timeStamp)

#  Wait until all the components are finished.
        self.services.wait_call_list(self.running_components.values(), True)
