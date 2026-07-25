
"""
weight and avgPrice are given from the instantiation of the main product category
"""
class Product:
    def __init__(self, name: str, price: float):
	self.name = name
	self.price = price

products = [Product("salshisha", 0.5, 5)]

# The following class goes into the Simulation folder
class ProductDistributionIndex:
    def __init__(self, product, avg_price, weight):
        self.product = product
        self.avg_price = avg_price
        self.weight = weight
