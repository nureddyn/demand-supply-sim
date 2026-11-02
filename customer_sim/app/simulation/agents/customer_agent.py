from .agent import Agent


class CustomerAgent(Agent):
    def __init__(self, customer):
        self._customer = customer

    def observe(self):
        pass

    def decide(self):
        pass

    def act(self):
        pass
