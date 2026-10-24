from __future__ import annotations
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

        if not self.amount.is_finite():
            raise ValueError("Amount must be finite")

        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

    def __add__(self, summand: Money) -> Money:
        if self.currency != summand.currency:
            raise ValueError("Currency missmatch")

        return Money(amount=self.amount + summand.amount, currency=self.currency)

    def __sub__(self, subtrahend: Money) -> Money:
        if self.currency != subtrahend.currency:
            raise ValueError("Currency missmatch")

        return Money(amount=self.amount - subtrahend.amount, currency=self.currency)

    def __gt__(self, other: Money) -> bool:
        return self.amount > other.amount


"""
Usage:
money = Money(
    amount=Decimal("25.50"),
    currency="USD"
)
"""
# TODO: Validate currency and define rules for precision, rounding, and arithmetic operations.
