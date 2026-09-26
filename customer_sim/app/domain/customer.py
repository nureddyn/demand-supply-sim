from .AgentInterface import Agent

class Customer:
    def __init__(self):
        self.budget = 0.0
        self.wish_list = []

    def get_budget(self):
        return self.budget

    def set_budget(self, value):
        if value < 0:
            raise ValueError("Budget cannot be negative")
        if value == math.inf:
            raise ValueError("Budget cannot be max float or beyond")
        self.budget = value

    def request_products(self, store):
        products = store.get_products()
        return products

    def request_product(self, store, product_name):
        product = store.get_product(product_name)
        return product

    def add_product_to_cart(self, store, product_name, qty):
        ...

    def pay(self, store):
        ...

