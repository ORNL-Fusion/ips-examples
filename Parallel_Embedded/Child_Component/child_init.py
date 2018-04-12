#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for CHILD Init component.
#
#-------------------------------------------------------------------------------

from component import Component

#-------------------------------------------------------------------------------
#
#  CHILD Init Class
#
#-------------------------------------------------------------------------------
class child_init(Component):
    
#-------------------------------------------------------------------------------
#
#  CHILD Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('child_init: Construct')
        Component.__init__(self, services, config)

#-------------------------------------------------------------------------------
#
#  child_init Component init method. This method prepairs the input files. This
#  allows staging the plasma state files and creates the inital state.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('child_init: init')

#-------------------------------------------------------------------------------
#
#  child_init Component step method. This component does nothing and is
#  never called.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('child_init: step')

#-------------------------------------------------------------------------------
#
#  child_init Component finalize method. This cleans up afterwards. Not
#  used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('child_init: finalize')
