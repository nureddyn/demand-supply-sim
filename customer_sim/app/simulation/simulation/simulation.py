class Simulation:
    def __init__(self, scheduler, environment):
        # These parameters may be passed from the controller runtime
        self.scheduler = scheduler
        self.environment = environment

    def execute(self):
        self.scheduler.timing_routine(self.environment)
