# Use Pydantic to create an array of ProductDto
class ProductDto:
    def __init__(self, data):
        self.name = data["name"]
        self.price = data["price"]
        self.stock = data["stock"]
