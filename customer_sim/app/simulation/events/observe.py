from .event import Event

class Observe(Event):
    def __init__(self, agent)
        self.agent = agent

    def execute(self, environment):
        self.agent.observe(environment.get_view())

    def next_events():
        pass
