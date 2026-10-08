from app.domain.customer import Customer
from app.domain.budget import Budget

def test_customer_initialization():
    initial_budget = Budget(100.0)
    customer = Customer(initial_budget)

    assert customer.budget == initial_budget
    assert customer.budget.value == 100.0

    assert customer.wish_list == []
