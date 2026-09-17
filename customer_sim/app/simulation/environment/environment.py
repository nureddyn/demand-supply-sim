
"""
Agent's environment

This class should contain the market's model, allowing initialization of customer's capital pool along with income
distribution, and the set of products in the market, the total value of the market, and a product distribution in the
market.
"""
# from utils.math.distributions import income_distribution
class Environment:
    def __init__(self):
        # self.store = storeClient()
        # self.global_products = globalProducts()
        # self.income_distribution = income_distribution()
        ...

    def get_view(self):
        return {"store": self.store, "global-products": self.global_products}

    def generate_budget(self):
        return self.income_distribution.generate_value()
