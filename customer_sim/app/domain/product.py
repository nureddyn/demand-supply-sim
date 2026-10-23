# TODO:Design product class
from app.domain.money import Money


class Product:
    def __init__(self, name: str, price: Money) -> None:
        self.name = name
        self.price = price
