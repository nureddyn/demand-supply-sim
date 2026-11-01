from .agent import Agent


class CustomerAgent(Agent):
    def __init__(self, customer):
        self._customer = customer
