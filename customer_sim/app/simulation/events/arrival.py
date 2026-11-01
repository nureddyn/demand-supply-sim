from app.simulation.events.event import Event
from app.domain.customer import Customer
from app.simulation.agents.customer_agent import CustomerAgent


class Arrival:
    def execute(self, environment):
        budget = environment.seed_budget()
        customer = Customer(budget)
        customer_agent = CustomerAgent(customer)
        environment.insert_agent_to_space(customer_agent)
