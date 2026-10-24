from app.domain.money import Money


class Customer:
    def __init__(self, budget: Money):
        self._budget = budget
        self.wish_list = []

    @property
    def budget(self):
        return self._budget

    def spend(self, amount: Money):
        if amount > self._budget:
            raise ValueError("Insufficient budget")
        self._budget = self._budget - amount
