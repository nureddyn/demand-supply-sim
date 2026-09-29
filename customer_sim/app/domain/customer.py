
class Customer:
    def __init__(self, budget):
        self.budget = budget
        self.wish_list = []

    def get_budget(self):
        return self.budget

    def set_budget(self, budget):
        self.budget = budget

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

