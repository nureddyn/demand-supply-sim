from decimal import Decimal

from app.domain.product import Product
from app.domain.money import Money

import pytest


@pytest.fixture
def product():
    return Product(name="mouse", price=Money(amount=Decimal("6.0"), currency="USD"))


def test_product_initialization(product):
    assert product.name == "mouse"
    assert product.price == Money(amount=Decimal("6.0"), currency="USD")


def test_product_set_price_valid_value(product):
    new_price = Money(amount=Decimal("4.0"), currency="USD")
    product.set_price(new_price)
    assert product.price == new_price
