#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for TEST Init component.
#
#-------------------------------------------------------------------------------

from component import Component
import subprocess

#-------------------------------------------------------------------------------
#
#  TEST Init Class
#
#-------------------------------------------------------------------------------
class test_framework_init(Component):
    
#-------------------------------------------------------------------------------
#
#  TEST Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('test_framework_init: Construct')
        Component.__init__(self, services, config)

#-------------------------------------------------------------------------------
#
#  test_framework_init Component init method. This method prepairs the input
#  files. This allows staging the plasma state files and creates the inital
#  state.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0):
        print('test_framework_init: init')

        self.platform_conf = self.services.get_config_param('PLATFORM_FILE')
        self.simulation_conf = self.services.get_config_param('TEST_COMPONENT_CONF')

#-------------------------------------------------------------------------------
#
#  test_framework_init Component step method. This component does nothing and is
#  never called.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('test_framework_init: step')

        process = subprocess.Popen(['ips.py', '--platform={}'.format(self.platform_conf), '--simulation={}'.format(self.simulation_conf)])
        process.wait();

#-------------------------------------------------------------------------------
#
#  test_framework_init Component finalize method. This cleans up afterwards. Not
#  used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('test_framework_init: finalize')
