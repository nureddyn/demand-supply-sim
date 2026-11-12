import pytest
import random
from app.domain.money import Money
from decimal import Decimal
from app.simulation.environment.environment import Environment


@pytest.fixture
def environment():
    return Environment()


def test_seed_budget(environment):
    random.seed(42)
    # seed_budget = environment.seed_budget()

    # Every case must be generated with environment.seed_budget()
    assert environment.seed_budget().amount == Decimal("63.942679845788376")
    assert environment.seed_budget().amount == Decimal("2.5010755222666936")
    assert environment.seed_budget().amount == Decimal("27.502931836911927")
