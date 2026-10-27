from dataclasses import FrozenInstanceError

from app.domain.money import Money
import pytest
import math
from decimal import Decimal


@pytest.fixture
def money():
    return Money(amount=Decimal("0.0"), currency="USD")


@pytest.mark.parametrize(
    "invalid_value, expected_msg",
    [
        (Decimal("-5.0"), "Amount cannot be negative"),
        (Decimal("0").next_minus(), "Amount cannot be negative"),
        (Decimal("NaN"), "Amount cannot be NaN"),
        (Decimal("Infinity"), "Amount must be finite"),
        (Decimal("-Infinity"), "Amount must be finite"),
    ],
)
def test_money_rejects_invalid_amounts(invalid_value, expected_msg):
    # Verify the constructor denies the value
    with pytest.raises(ValueError, match=expected_msg):
        Money(amount=invalid_value, currency="USD")


def test_money_is_immutable(money):
    with pytest.raises(FrozenInstanceError):
        money.amount = Decimal("50.0")


def test_set_money_zero_boundary_succeeds():
    money = Money(amount=Decimal("0.0"), currency="USD")
    assert money.amount == Decimal("0.0")


def test_set_money_positive_value_succeeds():
    """Verify a representative positive value within the valid domain"""
    money = Money(amount=Decimal("10.0"), currency="USD")
    assert money.amount == Decimal("10.0")


def test_valid_addition_between_money_instances(money):
    summand = Money(amount=Decimal("10.0"), currency="USD")
    total = money + summand
    assert total == Money(amount=Decimal("10.0"), currency="USD")


def test_invalid_addition_with_different_currency(money):
    summand = Money(amount=Decimal("25.0"), currency="EUR")
    with pytest.raises(ValueError, match="Currency missmatch"):
        money + summand


def test_valid_subtraction_between_money_instances():
    minuend = Money(amount=Decimal("21.5"), currency="USD")
    subtrahend = Money(amount=Decimal("8.0"), currency="USD")
    total = minuend - subtrahend
    assert total == Money(amount=Decimal("13.5"), currency="USD")


def test_greater_than_predicate(money):
    other = Money(amount=Decimal("6.3"), currency="USD")
    assert (other > money) == True
