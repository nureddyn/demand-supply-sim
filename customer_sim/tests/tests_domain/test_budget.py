from app.domain.budget import Budget, budget
import pytest
import math


@pytest.fixture
def budget():
    return Budget(0.0)


@pytest.mark.parametrize(
    "invalid_value, expected_msg",
    [
        (-5.0, "Budget cannot be negative"),
        (math.nextafter(0, -math.inf), "Budget cannot be negative"),
        (float("nan"), "Budget cannot be NaN"),
        (math.inf, "Budget cannot exceed maximum allowed float limit"),
        (
            math.nextafter(Budget.MAX_BUDGET, math.inf),
            "Budget cannot exceed maximum allowed float limit",
        ),
    ],
)
def test_set_budget_invalid_values_raise_error(budget, invalid_value, expected_msg):
    # Verify the constructor denies the value
    with pytest.raises(ValueError, match=expected_msg):
        Budget(invalid_value)
    # Verify set_value denies the value in an existing instance
    with pytest.raises(ValueError, match=expected_msg):
        budget.set_value(invalid_value)


def test_set_budget_zero_boundary_succeeds(budget):
    budget.set_value(0.0)
    assert budget.value == 0.0


def test_set_budget_positive_value_succeeds(budget):
    """Verify a representative positive value within the valid domain"""
    budget.set_value(10.0)
    assert budget.value == 10.0


def test_set_budget_highest_valid_float_succeeds(budget):
    """Verify the valid upper limit value"""
    valid_max = Budget.MAX_BUDGET
    budget.set_value(valid_max)
    assert budget.value == valid_max
