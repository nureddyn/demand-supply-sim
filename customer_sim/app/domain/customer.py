from .AgentInterface import Agent

class Customer:
    def __init__(self, budget):
        if budget <= 0:
            raise ValueError("initial budget cannot be negative or 0")
        self.budget = budget
        self.wish_list = []

    def get_budget(self):
        ...

    def set_budget(self, value):
        if value < 0:
            raise ValueError("Budget after purchase cannot be negative")
        self.budget = value

    def request_products(store):
        products = store.get_products()
        return products

    def request_product(store, product_name):
        product = store.get_product(product_name)
        return product

    def add_product_to_cart(store, product_name, qty):
        ...

    def pay(store):
        ...

