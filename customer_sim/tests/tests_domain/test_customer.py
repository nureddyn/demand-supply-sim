from app.domain.customer import Customer

def test_customer_initialization():
    initial_budget = 100.0
    customer = Customer(initial_budget)

    assert customer.budget == initial_budget

    assert customer.wish_list == []
