from ...app.domain.customer import Customer
from unittest.mock import Mock

class TestCustomer:
    def test_constructor(self):
        instance = Customer(10)

        assert instance.budget == 10
        assert instance.wish_list == []


    def test_request_products(self):
        instance = Customer(5)
        mock_store = Mock()

        # Test Case: Normal list of products
        mock_product_1 = Mock()
        mock_product_2 = Mock()
        mock_product_list = [mock_product_1, mock_product_2]

        mock_store.get_products.return_value = mock_product_list

        result = instance.request_products(mock_store)


        assert result == mock_product_list
        assert len(result) == 2


        # Test Case: empty list of products.
        # This depends on how the store service handle edge cases like failure in fetching data
        # ...

        # Test Case: ensure get_products method did interact with the mocked store service
        mock_store.get_products.assert_called_once()

