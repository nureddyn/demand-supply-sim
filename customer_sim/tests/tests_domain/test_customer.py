from ...app.domain.customer import Customer
import Budget
from unittest.mock import Mock
import math


def test_customer_initialization():
    initial_budget = Budget(100.0)
    customer = Customer(initial_budget)

    assert customer.get_budget() == initial_budget
    assert customer.get_budget().value == 100.0

