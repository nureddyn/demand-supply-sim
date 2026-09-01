from ...app.domain.customer import Customer
from unittest.mock import Mock

#TODO:
"""
Define the test approach for the unit. It is important to make an informal domain analysis to pinpoint the values'
intervals of each class field along with their respective class invariants and restrictions. For example, if a domain
rule determines that the minimum possible value for 'budget', when the class is instantiated, must be the lowest market
price of a product in the global product category, then that rule will influence the design of test cases.


Examples of test approaches can be "Equivalence Partitioning" and "Bounded Value testing".

It might be better to do the domain analysis for the budget testing data at the environment level or above, where
the budget generation logic is located. In that case, input data for the constructor of Customer can be in some sense
arbitrary, focusing on correct initialization and correct method functionality.
"""

class TestCustomer:
    def test_constructor(self):
        test_budget_data = 10
        instance = Customer(test_budget_data)

        assert instance.budget == 10
        assert instance.wish_list == []


    def test_request_products(self):
        instance = Customer(5)
        mock_store = Mock()

        # Test Case: Normal list of products
        mock_product_1 = Mock()
        mock_product_2 = Mock()
        # It doesn't matter if the instance has no elements in 'wish_list', the important here is to check if the
        # method correctly calls the internal function that request and receive the data requested 
        mock_product_list = [mock_product_1, mock_product_2]

        mock_store.get_products.return_value = mock_product_list

        result = instance.request_products(mock_store)


        assert result == mock_product_list
        assert len(result) == 2


        # Test Case: empty list of products.
        # This depends on how the store service handle edge cases like failure in fetching data
        # ...
        #TODO

        # Test Case: ensure get_products method did interact with the mocked store service
        mock_store.get_products.assert_called_once()

    def test_request_product(self):
        instance = Customer(20)
        mock_store = Mock()
        mock_product = Mock()

        mock_product = mock_product

        mock_store.get_product.return_value = mock_product

        result = instance.request_product(mock_store, mock_product)

        assert result == mock_product

        mock_store.get_product.assert_called_once()

