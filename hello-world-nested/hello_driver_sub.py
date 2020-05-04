#-------------------------------------------------------------------------------
# Copyright 2006-2012 UT-Battelle, LLC. See LICENSE for more information.
#-------------------------------------------------------------------------------
import os

from  component import Component

class HelloDriver(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print('Created %s' % (self.__class__))

    def init(self, timeStamp=0.0):
        return

    def validate(self, timeStamp=0.0):
        return

    def step(self, timeStamp=0.0):
        try:
            worker_comp = self.services.get_port('WORKER')
        except Exception:
            self.services.exception('Error accessing worker component')
            raise
        self.services.call(worker_comp, 'step', 0.0)
        open(self.OUTPUT_FILES[0], 'w').write("SUB OUTPUT FILE\n")
        self.services.stage_output_files(timeStamp, self.OUTPUT_FILES)
        return

    def finalize(self, timeStamp=0.0):
        return
