from .agent import Agent


class CustomerAgent(Agent):
    def __init__(self, customer):
        self.customer = customer
        self.memory = []
        self.current_goal = ""
        ...

    def observe(self, env): ...

    def decide(self, observation): ...

    def act(self, observation): ...
