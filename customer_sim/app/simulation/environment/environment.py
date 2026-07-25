
"""
Agent's environment
"""

class Environment:
    def __init__(self, income_distribution):
        # self.store = storeClient()
        # self.global_products = globalProducts()
        # self.income_distribution = income_distribution
        ...

    def get_view(self):
        return {"store": self.store, "global-products": self.global_products}

    def generate_budget(self):
        ...
