from .AgentInterface import Agent

class Customer:
    def __init__(self, budget):
        self.budget = budget
        self.wish_list = []

    def get_budget(self):
        ...

    def set_budget(self, value):
        ...

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

