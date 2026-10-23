import math
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if math.isnan(self.amount):
            raise ValueError("Amount cannot be NaN")

        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

        if not self.amount.is_finite():
            raise ValueError("Amount must be finite")


"""
Usage:
money = Money(
    amount=Decimal("25.50"),
    currency="USD"
)
"""

# TODO: Validate currency and define rules for precision, rounding, and arithmetic operations.
