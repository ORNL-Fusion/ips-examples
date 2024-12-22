#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for TEST Init component.
#
#-------------------------------------------------------------------------------

from component import Component

#-------------------------------------------------------------------------------
#
#  TEST Init Class
#
#-------------------------------------------------------------------------------
class test_componet_init(Component):
    
#-------------------------------------------------------------------------------
#
#  TEST Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('test_componet_init: Construct')
        Component.__init__(self, services, config)

#-------------------------------------------------------------------------------
#
#  test_componet_init Component init method. This method prepairs the input files. This
#  allows staging the plasma state files and creates the inital state.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('test_componet_init: init')

#-------------------------------------------------------------------------------
#
#  test_componet_init Component step method. This component does nothing and is
#  never called.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('test_componet_init: step')

#-------------------------------------------------------------------------------
#
#  test_componet_init Component finalize method. This cleans up afterwards. Not
#  used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('test_componet_init: finalize')
