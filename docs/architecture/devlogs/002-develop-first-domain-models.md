#### General Context

The goal of this phase is to begin developing the first classes of the business domain, where each class is defined with a set of fields and methods sufficient to implement the development cycle and continuous integration (CI). Recall that the system's business domain consists of the classes and rules governing the interaction between buyers and the store.


### Task 1 — Creation of working branch and required folder

###### Process and Decisions:

1. The branch created for this phase is `design/domain-models`.

2. **Creating the necessary folders for development:** We must remember that the established infrastructure configuration requires us to develop with test/code coverage; that is, for each unit under development, its respective unit test is developed in parallel. Therefore, we create the `domain/` folder in `customer-sim/app`, and the `tests_domain/` folder in `customer-sim/tests`.


### Task 2 — Design and development of Customer and Budget classes

###### Process and Decisions:

1. **Implementation of `Customer` class**

- `Customer` will have the fields `budget` and `wish_list`. This decision is made because, generally speaking, every customer will interact with the store when requesting a product of interest contained in their wish list and performing a cost calculation that considers the product's in-store price against their current budget. As for the methods, we will start with just the `getter` and `setter` of `budget`.
