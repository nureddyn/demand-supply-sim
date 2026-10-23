from app.domain.customer import Customer
from app.domain.money import Money
from decimal import Decimal


def test_customer_initialization():
    initial_money = Money(amount=Decimal("100.0"), currency="USD")
    customer = Customer(initial_money)

    assert customer.money == initial_money
    assert customer.money.amount == Decimal("100.0")

    assert customer.wish_list == []
