from app.simulation.events.event import Event
from app.domain.customer import Customer
from app.simulation.agents.customer_agent import CustomerAgent


class Arrival(Event):
    def __init__(self) -> None:
        agent_id: int | None = None

    def execute(self, environment):
        budget = environment.seed_budget()
        customer = Customer(budget)
        customer_agent = CustomerAgent(customer)
        agent_id = environment.add_agent(customer_agent)
        self._set_agent_id(agent_id)

    def _set_agent_id(self, id: int):
        self.agent_id = id

    def next_events(self):
        pass
