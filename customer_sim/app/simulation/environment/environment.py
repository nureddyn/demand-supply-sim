from app.domain.money import Money
from app.simulation.agents.agent import Agent
from decimal import Decimal
import random
from itertools import count


class Environment:
    def __init__(self) -> None:
        self._current_id = count(0)
        self.agent_space: dict[int, Agent]

    def seed_budget(self):
        return Money(amount=Decimal(str(random.uniform(0.0, 100.0))), currency="USD")

    def add_agent(self, agent):
        id = self._generate_agent_id()
        self.agent_space[id] = agent
        return id

    def _generate_agent_id(self):
        return next(self._current_id)
