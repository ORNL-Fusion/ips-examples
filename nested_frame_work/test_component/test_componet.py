#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for TEST component.
#
#-------------------------------------------------------------------------------

from component import Component
import time

#-------------------------------------------------------------------------------
#
#  TEST Class
#
#-------------------------------------------------------------------------------
class test_componet(Component):
    
#-------------------------------------------------------------------------------
#
#  TEST Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('test_componet: Construct')
        Component.__init__(self, services, config)
        self.running_tasks = {}

#-------------------------------------------------------------------------------
#
#  TEST Component init method. This method prepairs the input files.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('test_componet: init')

        if 'message' in keywords:
            self.message = keywords['message']
        else:
            self.message = 'Hello'

#-------------------------------------------------------------------------------
#
#  TEST Component step method. This runs code the component is wrapped around.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('test_componet: step')
    
#  Launch a task. Task launches are non blocking so save the task id. Depending
#  on the system, install locations and binary names can be different. Note, I'm
#  using the log file as an output since it pipes output there.
        self.running_tasks['test_componet_task'] = self.services.launch_task(self.NPROC,
                                                                             self.services.get_working_dir(),
                                                                             self.TEST_COMPONENT_EXE,
                                                                             self.message,
                                                                             logfile = 'log.test_componet')
    
#  Wait for tasks to complete.
        time.sleep(5)
        self.services.wait_tasklist(self.running_tasks.values(), True)
        self.running_tasks = {}
    
#-------------------------------------------------------------------------------
#
#  TEST Component finalize method. This cleans up afterwards. Not used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('test_componet: finalize')
        
        self.services.wait_tasklist(self.running_tasks.values(), True)
        self.running_tasks = {}
