
"""
Agent's environment
"""

class Environment:
    def __init__(self, income_distribution, product_choice_distribution):
        # self.store = storeClient()
        # self.global_products = globalProducts()
        # self.income_distribution = income_distribution
        ...

    # this is is not necessary, since representation should be internal to the agent
    def representation(self):
        return {"store": self.store, "global-products": self.global_products}

    def generate_budget(self, income_distribution):
        # this method could be used to give budget to a customer
        ...
