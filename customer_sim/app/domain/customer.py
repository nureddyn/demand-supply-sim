from app.domain.money import Money


class Customer:
    def __init__(self, money: Money):
        self.money = money
        self.wish_list = []

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money
