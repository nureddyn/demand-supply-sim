# TODO:Design product class
from app.domain.money import Money


class Product:
    def __init__(self, name: str, price: Money) -> None:
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def set_price(self, new_price: Money):
        self._price = new_price
