from __future__ import annotations
import math
from dataclasses import dataclass
from decimal import Decimal
from re import sub


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
        self._check_currency_match(summand)
        return Money(amount=self.amount + summand.amount, currency=self.currency)

    def __sub__(self, subtrahend: Money) -> Money:
        self._check_currency_match(subtrahend)
        return Money(amount=self.amount - subtrahend.amount, currency=self.currency)

    def _check_currency_match(self, other: Money):
        if self.currency != other.currency:
            raise ValueError("Currency missmatch")

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
