from app.simulation.events.arrival import Arrival
import pytest


@pytest.fixture
def arrival():
    return Arrival()


def test_execute_calls_dependencies_correctly(arrival, mocker):
    manager = mocker.MagicMock()

    mock_environment = mocker.MagicMock(spec=["seed_budget", "add_agent"])
    mock_customer = mocker.patch("app.simulation.events.arrival.Customer")
    mock_customer_agent = mocker.patch("app.simulation.events.arrival.CustomerAgent")

    manager.attach_mock(mock_environment, "environment")
    manager.attach_mock(mock_customer, "customer")
    manager.attach_mock(mock_customer_agent, "customer_agent")

    arrival.execute(mock_environment)

    mock_seed_budget_created_instance = mock_environment.seed_budget.return_value
    mock_customer_created_instance = mock_customer.return_value
    mock_customer_agent_created_instance = mock_customer_agent.return_value

    assert manager.mock_calls == [
        mocker.call.environment.seed_budget(),
        mocker.call.customer(mock_seed_budget_created_instance),
        mocker.call.customer_agent(mock_customer_created_instance),
        mocker.call.environment.add_agent(mock_customer_agent_created_instance),
    ]


def test_execute_updates_agent_id_correctly(arrival, mocker):
    mock_environment = mocker.MagicMock(spec=["seed_budget", "add_agent"])

    mock_environment.add_agent.return_value = 1

    assert arrival.agent_id == None

    arrival.execute(mock_environment)

    assert arrival.agent_id == 1
