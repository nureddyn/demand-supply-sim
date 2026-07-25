from .product_dto import ProductDto

# Here we are going to code the connection with the store service

class StoreClient:
    def __init__(self):
        pass

    def get_products(self):
	# This array of objects mocks a JSON received from the store service
        json_products = [{}]
        products = self.to_products(json_products)
        return products

    def to_products(self, json_products):
        products = []
        for i in range(len(json_products)):
            products.append(ProductDto(json_products[i]))
        return products

    def get_product(self, product_name):
        # Mocked product
        json_product = [{"name": product_name, "price": 1, "stock": 1}]
        return ProductDto(json_product)

