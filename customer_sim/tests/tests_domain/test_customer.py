from app.domain.budget import Budget
from app.domain.customer import Customer


def test_customer_initialization():
    initial_budget = Budget(100.0)
    customer = Customer(initial_budget)

    assert customer.get_budget() == initial_budget
    assert customer.get_budget().value == 100.0

    assert customer.wish_list == []
