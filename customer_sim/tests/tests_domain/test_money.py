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


def test_set_money_zero_boundary_succeeds(money):
    money.value = 0.0
    assert money.value == 0.0


def test_set_money_positive_value_succeeds(money):
    """Verify a representative positive value within the valid domain"""
    money.value = 10.0
    assert money.value == 10.0


def test_set_money_highest_valid_float_succeeds(money):
    """Verify the valid upper limit value"""
    valid_max = Money.MAX_BUDGET
    money.value = valid_max
    assert money.value == valid_max
