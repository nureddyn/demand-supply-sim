# import timing_routine

class Simulation:
    def __init__(self, scheduler, environment):
        self.scheduler = scheduler
        self.environment = environment

    def execute(self):
        self.scheduler.timing_routine.execute(self.environment)
