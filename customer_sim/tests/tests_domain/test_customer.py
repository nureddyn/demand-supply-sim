from app.domain.customer import Customer
from app.domain.money import Money
from decimal import Decimal
import pytest


@pytest.fixture
def customer():
    return Customer(Money(amount=Decimal("80.0"), currency="USD"))


def test_customer_initialization():
    initial_money = Money(amount=Decimal("100.0"), currency="USD")
    customer = Customer(initial_money)

    assert customer.budget == initial_money
    assert customer.budget.amount == Decimal("100.0")

    assert customer.wish_list == []


def test_customer_spend_valid_money(customer):
    current_budget = customer.budget
    money_spent = Money(amount=Decimal("20.0"), currency="USD")
    customer.spend(money_spent)
    assert customer.budget == current_budget - money_spent


def test_customer_spend_more_money_than_budget(customer):
    money_spent = Money(amount=Decimal("90.0"), currency="USD")
    with pytest.raises(ValueError):
        customer.spend(money_spent)
