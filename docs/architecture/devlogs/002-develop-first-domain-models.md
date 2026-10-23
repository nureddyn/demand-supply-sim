#### General Context

The goal of this phase is to begin developing the first classes of the business domain, where each class is defined with a set of fields and methods sufficient to test the development cycle and continuous integration (CI). Recall that the system's business domain consists of the classes and rules governing the interaction between buyers and the store.


### Task 1 — Creation of working branch and required folder

###### Process and Decisions:

1. The branch created for this phase is `design/domain-models`.

2. **Creating the necessary folders for development:** We must remember that the established infrastructure configuration requires us to develop with test/code coverage; that is, for each unit under development, its respective unit test is developed in parallel. Therefore, we create the `domain/` folder in `customer-sim/app`, and the `tests_domain/` folder in `customer-sim/tests`.


### Task 2 — Design and development of Customer and Budget classes

###### Process and Decisions:

1. **Implementation of `Customer` class**

- `Customer` will have the fields `budget` and `wish_list`. This decision is made because, generally speaking, every customer will interact with the store when requesting a product of interest contained in their wish list and performing a cost calculation that considers the product's in-store price against their current budget. As for the methods, we will start with just the `getter` and `setter` of `budget`.
- Made a basic implementation of `test_customer` to test the constructor, starting with the `budget` field as a `Float` primitive value. Later, when implemented `Budget` as a data object, we will update the test to to account for that change.
- Run `docker compose build customer_sim` to rebuild the container, and then run tests with `docker compose run --rm customer_sim pytest .`, passing successfully.
- Realized that the contents of `Makefile` does not include a command for testing with `pytest`. Added the corresponding block of code to run all tests with `make test`. After running the command, all tests passed.

2. **Implementation of `Budget` class**

- Implemented `Budget` as a value object class. This decision is made to locate the invariants of its allowed values and basic methods in one place, resulting in a more organized code. Another advantage of value objects is that they should be implemented as immutable objects, preventing the possibility of unwanted side effects, and promoting data integrity.

- Updated tests for `test_customer`: Consider budget as an object, parameterized invalid values determined by Budget invariants, and added tests for valid and invalid values of budget, using Equivalence Partitioning.

- Rebuilt `customer_sim` container and run tests. Found out that `test_budget` was failing due to two main factors:
  1. Incorrect way of calling the accessor and modifier methods (`Budget` is using the `@property` decorator).
  2. The invariants were not being executed when `budget.value` modifier was called.


### Task 3 — Design and development of Product class

###### Process and Decisions:

- Although we haven't defined the context in which a `Product` instance will be created, nor the appropriate mechanism to identify each product instance in the simulation, we can start by defining `name` and `price` as its fields. A problem that already emerges as common between the `Customer` and `Product` classes is that both have a field that could potentially be of the same data type; `Customer.budget` and `Product.price` could both be considered `Money`.

- This approach involves renaming the `Budget` class to `Money`, modifying `Product` so that the `price` field is of type `Money`, modifying `Customer` so that the `budget` field is also of type `Money`, and modifying `Money` so that it effectively becomes an immutable value object. Finally, we must also change the import names from all files involved, including test files. For representing monetary amounts, it has been decided to use `decimal` instead of `float`, thereby avoiding precision issues associated with the binary representation of decimal numbers.
