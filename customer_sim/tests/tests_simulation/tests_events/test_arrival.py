from app.simulation.events.arrival import Arrival
import pytest


@pytest.fixture
def arrival():
    return Arrival()


def test_execute_calls_dependencies_correctly(arrival, mocker):
    mock_environment = mocker.MagicMock(spec=["seed_budget", "add_agent"])
    mock_customer = mocker.patch("app.simulation.events.arrival.Customer")
    mock_customer_agent = mocker.patch("app.simulation.events.arrival.CustomerAgent")

    arrival.execute(mock_environment)

    mock_customer_created_instance = mock_customer.return_value
    mock_customer_agent_created_instance = mock_customer_agent.return_value

    mock_environment.seed_budget.assert_called_once()
    mock_customer.assert_called_once()
    mock_customer_agent.assert_called_once_with(mock_customer_created_instance)
    mock_environment.add_agent.assert_called_once_with(
        mock_customer_agent_created_instance
    )
