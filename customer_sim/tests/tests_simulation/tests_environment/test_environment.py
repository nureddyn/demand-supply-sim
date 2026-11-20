import pytest
import random
from app.domain.money import Money
from decimal import Decimal
from app.simulation.environment.environment import Environment
from app.simulation.agents.customer_agent import CustomerAgent
from app.domain.customer import Customer


@pytest.fixture
def environment():
    return Environment()


def test_seed_budget(environment):
    random.seed(42)
    # seed_budget = environment.seed_budget()

    # Every case must be generated with environment.seed_budget()
    assert environment.seed_budget().amount == Decimal("63.942679845788376")
    assert environment.seed_budget().amount == Decimal("2.5010755222666936")
    assert environment.seed_budget().amount == Decimal("27.502931836911927")


def test_add_agent_assigns_sequential_ids(environment):
    # Instantiate two agents
    agent1 = CustomerAgent(Customer(Money(amount=Decimal("10.0"), currency="USD")))
    agent2 = CustomerAgent(Customer(Money(amount=Decimal("30.0"), currency="USD")))

    # Add agents to environment
    agent_id_1 = environment.add_agent(agent1)
    agent_id_2 = environment.add_agent(agent2)

    # Check whether each agent has been assigned their corresponding id
    assert agent_id_1 == 1
    assert agent_id_2 == 2

    # Check whether each agent was correctly saved in agent_space
    assert environment.agent_space[agent_id_1] == agent1
    assert environment.agent_space[agent_id_2] == agent2
