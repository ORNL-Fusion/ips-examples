#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for CHILD component.
#
#-------------------------------------------------------------------------------

from component import Component
import time

#-------------------------------------------------------------------------------
#
#  CHILD Class
#
#-------------------------------------------------------------------------------
class child(Component):
    
#-------------------------------------------------------------------------------
#
#  CHILD Init Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('child: Construct')
        Component.__init__(self, services, config)
        self.running_tasks = {}

#-------------------------------------------------------------------------------
#
#  child Component init method. This method prepairs the input files.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('child: init')

        if 'message' in keywords:
            self.message = keywords['message']
        else:
            self.message = 'Hello'

#-------------------------------------------------------------------------------
#
#  child Component step method. This runs code the component is wrapped around.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('child: step')
    
#  Launch a task. Task launches are non blocking so save the task id. Depending
#  on the system, install locations and binary names can be different. Note, I'm
#  using the log file as an output since it pipes output there.
        self.running_tasks['child_task'] = self.services.launch_task(self.NPROC,
                                                                     self.services.get_working_dir(),
                                                                     self.CHILD_EXE,
                                                                     self.message,
                                                                     logfile = 'log.child')
    
#  Wait for tasks to complete.
        time.sleep(30)
        self.services.wait_tasklist(self.running_tasks.values(), True)
        self.running_tasks = {}
    
#-------------------------------------------------------------------------------
#
#  child Component finalize method. This cleans up afterwards. Not used.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('child: finalize')
        
        self.services.wait_tasklist(self.running_tasks.values(), True)
        self.running_tasks = {}
