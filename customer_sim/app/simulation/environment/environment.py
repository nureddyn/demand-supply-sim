from app.domain.money import Money
from decimal import Decimal
import random


class Environment:
    def seed_budget(self):
        return Money(amount=Decimal(str(random.uniform(0.0, 100.0))), currency="USD")
