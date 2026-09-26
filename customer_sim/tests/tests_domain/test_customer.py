from ...app.domain.customer import Customer
from unittest.mock import Mock
import math

#TODO:
"""
How to test this unit:
- Examples of test approaches can be "Equivalence Partitioning" and "Bounded Value testing".
- Equivalent Partitioning for 'budget':
    We need to distinguish between initialization values and and the invariants that will govern how 'budget' will
    change in value over the lifetime of the object.
    - Initialization values:
        - Float Values:
            - Invalid lower interval: [-math.inf, 0]. Partition representative: budget = -10
            - Invalid upper interval: math.inf
            - Valid interval: [math.nextafter(0, math.inf), math.nextafter(math.inf, -math.inf)]
              # The above means (0, LARGEST_VALID_FLOAT]

"""

class TestCustomer(unittest.TestCase):
    def test_constructor(self):
        instance = Customer()
        assert instance.budget == 0.0
        assert instance.wish_list == []

    def get_budget(self):
        instance = Customer()
        assert instance.get_budget() == 0.0

        instance = Customer()
        instance.budget = 20.0
        assert instance.get_budget() == 20.0

    # Tests: set_budget
    def test_set_budget_negative_float(self):
        instance = Customer()
        test_budget_data = -5.0
        with self.assertRaises(ValueError):
            instance.set_budget(test_budget_data)

    def test_set_budget_invalid_lower_limit(self):
        instance = Customer()
        test_budget_data = math.nextafter(0.0, -math.inf)
        with self.assertRaises(ValueError):
            instance.set_budget(test_budget_data)

    def test_set_budget_valid_lower_limit(self):
        instance = Customer()
        test_budget_data = 0.0
        instance.set_budget(test_budget_data)
        assert instance.budget == 0.0

    def test_set_budget_valid_nominal_value(self):
        instance = Customer()
        test_budget_data = 10.0
        instance.set_budget(test_budget_data)
        assert instance.budget == 10.0

    def test_set_budget_valid_upper_limit(self):
        instance = Customer()
        test_budget_data = math.nextafter(math.inf, -math.inf)
        instance.set_budget(test_budget_data)
        assert instance.budget == math.nextafter(math.inf, -math.inf)

    def test_set_budget_invalid_upper_limit(self):
        instance = Customer()
        test_budget_data = math.inf
        with self.assertRaises(ValueError):
            instance.set_budget(test_budget_data)


    def test_request_products(self):
        # ---- Tests to work with ----

        instance = Customer()
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


        # Test Case: ensure get_products method did interact with the mocked store service
        mock_store.get_products.assert_called_once()

        # ---- End Tests to work with ----


        # Test Case: empty list of products.
        # This depends on how the store service handle edge cases like failure in fetching data
        # ...
        #TODO


    def test_request_product(self):
        instance = Customer()
        mock_store = Mock()
        mock_product = Mock()

        mock_product = mock_product

        mock_store.get_product.return_value = mock_product

        result = instance.request_product(mock_store, mock_product)

        assert result == mock_product

        mock_store.get_product.assert_called_once()




"""

        # Valid nominal value
        test_budget_data = 10
        instance = Customer(test_budget_data)

        assert instance.budget == 10
        assert instance.wish_list == []

        # Valid lower bound (+min)
        test_budget_data = math.nextafter(0, math.inf)

        assert instance.budget == math.nextafter(0, math.inf)
        assert instance.wish_list == []


        # Valid upper bound (-max)
        test_budget_data = math.nextafter(math.inf, -math.inf)

        assert instance.budget == math.nextafter(math.inf, -math.inf)
        assert instance.wish_list == []


        # Invalid budget value
        test_budget_data = -10

        with self.assertRaises(ValueError):
            instance = Customer(test_budget_data)

        # Invalid lower bound (-min)
        test_budget_data = 0

        with self.assertRaises(ValueError):
            instance = Customer(test_budget_data)

        # Invalid upper bound (+max)
        test_budget_data = math.inf + math.nextafter(0, math.inf)

"""
