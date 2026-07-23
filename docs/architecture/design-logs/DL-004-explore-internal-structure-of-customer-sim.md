**date:** 2026-07-20
**System Context:** Project bootstrap — customer-sim internal organization
**Design Criterion:** Design exploration (design-driven)

---
### Context

In this log, the `customer-sim` layer is explored, focusing on its purpose, core abstractions, and interaction with the rest of the system. The goal is to experiment with module-level designs, model key entities and behaviors, and evaluate their impact on system structure.

At this stage, the primary quality attribute is **maintainability**, understood as:
- ease of testing simulation and domain logic in isolation
- ease of modifying behavior without affecting unrelated components
- clarity of the model (readability and conceptual alignment with the domain)

Because maintainability is assessed by observing how easily the system accommodates new features and changes over time, meaningful response measures can only be established once the system has evolved beyond its initial structure.

Furthermore, domain knowledge will be used to guide modeling decisions, particularly in how customer behavior and demand are represented.

Finally, it is worth noting that the descriptions provided below are not intended to commit the design to specific structures, and that the details regarding content and implementation will take shape during the development process itself.

  ---
### `customer-sim` layers

While writing this log, it was decided to experiment with the overall structure and how each module would be organized within the `customer-sim/app` folder. In order to make the different service levels visible based on their concern, it was decided to organize the application into the following layers, which group the elements of each level of abstraction:

- **Domain:** Core business logic, which includes models related to demand, such as `customer` and `product`.
- **Simulation:** This layer contains the core of the simulation’s execution. Here, models and processes related to the simulation are defined, such as the scheduler, events, environment, etc. 
- **Infrastructure:** This layer defines the APIs that will enable interaction with other services (`store`, `DB`, etc.).
- **User Interface:** The layer that defines how the user interacts with the system.

As will become clear later, when comparing the `domain` layer and the `simulation` layer, we will see that `simulation` serves as a technical subdomain, more specifically, the simulation engine responsible for running experiments.

In the following section, we will go through each of the layers described above, defining some of their corresponding classes.


#### Domain Layer

##### Customer:

This class models the basic data for any buyer, as well as the methods directly associated with interacting with the store:

``` mermaid
classDiagram
    class Customer{
        -budget: __Float__
        -wish_list: __List__
        +request_product()
        +add_to_cart()
        +pay()
    }
```

In general, customers and their preferences can vary, directly influencing behavior. As a result, this class can later be converted into an interface or base class that models behavior shared among different customer profiles.


##### Product:

The basic product class, containing only business data and logic. Although we are going to use probability distributions to allow the process of random product selection, this class may be complemented with a product distribution indexer.

``` mermaid
classDiagram
	class Product{
	-name: __String__
	-price: __Float__
	}
```

---
#### Simulation Layer

##### Agent:

Let's define the abstract class `Agent`, which will represent all types of agents that a demand simulation might have, describing the general behavior that characterizes an agent, namely: `observe`, `decide`, `act`. 

``` mermaid
classDiagram
	class Agent{
	<<abstract class>>
	+observe(env: __Environment__)
	+decide()
	+act()
	}

	class CustomerAgent{
		-customer: __Customer__
		-memory
		...
	}

	Agent <|.. CustomerAgent : implements
```

As the `Agent` base class states, each customer's behavior involves a process of observation, decision-making, and interaction with their environment and the store system, serving as the actor of individual demand.

Naturally, the specific implementation of `Agent` for this iteration will be `CustomerAgent`. The idea is that `CustomerAgent` and `Customer` (the model found in the domain) would create a relationship that can be either of aggregation or composition, being `CustomerAgent` focused on modeling agent behavior. As you can see, this approach helps us meet our goal of maintainability by separating domain logic from simulation logic, enabling greater decoupling and facilitating testing.

``` mermaid
classDiagram
CustomerAgent *-- Customer

	class CustomerAgent{
		-customer: __Customer__
		-memory
		...
	}
	
	class Customer{
        -budget: __Float__
        -wish_list: __List__
    }
```


##### Simulation:

This class centralizes the execution of the simulation, managing the _scheduler_, and potentially initializing user configurations, statistical counters, etc.

``` mermaid
classDiagram
	class Simulation{
		-scheduler: __Scheduler__
		-environment: __Environment__
		+execute() __void__
	}
```


##### Scheduler:

The `Scheduler` acts as a runtime state machine, tracking simulated time, managing the loop (`timing_routine`) and events, and allowing the domain entities and the simulation state to be updated.

``` mermaid
classDiagram
	class Scheduler{
		-clock: __Clock__
		-event_list: __EventList__
		-advance_time(new_time: __Clock__)
		+timing_routine()
	}
```


##### Event List:

The `EventList` class contains the simulation events, allowing to add, extract, and sort events based on their respective simulated times. Because the time of occurrence of the events determines the order in which they are executed in the simulation run, a priority queue is the leading candidate for its implementation, which allows data to be sorted and retrieved efficiently based on its relative importance (e.g., maximum or minimum value). In our specific context, the implementation of a priority queue would let us retrieve the event with the least occurrence time in __O(1)__ (constant execution time).

``` mermaid
classDiagram
	class PriorityQueue{
	-data: List
	+insert(element)
	+extract_min()
	}
	class EventList{
		+insert_many(events: EventList)
	}
	PriorityQueue <|.. EventList
```


##### Event:

Events encapsulate state transitions in the simulation. Each event is initialized by receiving the clock (current simulated time) and internally generating its own simulated time of occurrence.

In addition, the abstract class `Event` declares that all events causally trigger new events. For example, it is reasonable to assume that the occurrence of the `Arrival` event determines the occurrence of the `RequestProduct` event (you cannot request a product if you have not yet reached the store); therefore, once the `Arrival` event occurs, new events dependent on it are generated (_RequestProduct_, _Observe_, etc.).

``` mermaid
classDiagram
	class Event{
		<<abstract class>>
		+next_events()
		+execute()
	}

	class Arrival{
	-time: __Clock__
	+next_events()
	+execute()
	}
	Event <|-- Arrival : Implements
```


##### Environment:

This class is intended to provide access to the store, the set of global products, and, potentially, attributes and methods for generating and setting environmental conditions probabilistically, such as income distribution, fluctuations in a product’s average market price, product choice distribution, etc. The idea here is to be able to model the market context within which agents operate, as well as each agent’s initial conditions.

``` mermaid
classDiagram
class Environment{
	-store
	-global_products
	+generate_budget(income_distribution: Distribution)
}
```

As shown in the class diagram above, a possible implementation of `Environment` would include a method to randomly generate a budget for a specific customer at the exact moment the customer's instance is initialized.

---
#### Infrastructure

The infrastructure layer defines how the simulation service interacts with its database and with the store service. Below, we will describe some of the elements that make up this layer, without going into too much detail, since the design here will depend largely on the design of its counterpart in the store service and on the implementation of the domain models and the simulation layer.


##### Store Client:

This class is expected to serve as the endpoint for each agent's interaction with the store, defining the available HTTP methods. Since we will be working exclusively with the simulation service at this stage, the implementation will essentially be a mock.

``` mermaid
classDiagram
class StoreClient{
	+get_products()
	+get_product(product_name)
	+add_to_cart(customer, product)
	+checkout(customer)
}
```


##### Database:

This module is expected to define the models that enable interaction with database entities, as well as the connection to the database and the various available transactions.

We can refer to the complete execution of a simulation as a “run” or “experiment,” which serves as a block of information that we can store in the database. These experiments may contain their respective statistical counters, user configurations, and any metadata that is relevant for subsequent analysis or evaluation. However, at this stage, we will not consider whether the final version of this service will be implemented so that each simulation runs in a single time block without interruption, or whether it will be possible to save the state of a simulation, allowing the user to pause and resume it as they see fit. For now, the simplest design approach would be to assume the first option and leave the pause and resume feature as a decision for a future redesign.

Because the models to be presented in this layer will depend on how the data is structured in the `domain/` and `simulation/` layers, these models will also be postponed to a future design log.

---
#### User Interface

This layer defines how the user will interact with the simulation service. Although its implementation is still under consideration, one option that has emerged is a command-line interface (CLI) structured according to the MVC (Model-View-Controller) pattern, which separates the system model, its representation to the user, and the commands available to the user. It has been decided that the user interface design will be covered in a future design log.

---

To conclude, let's take a look at how the folder structure for the four layers described earlier would be organized:

```
customer-sim

Domain
 ├── Customer
 └── Product

Simulation
 ├── Simulation
 ├── Scheduler
 ├── Event
 ├── EventList
 ├── Environment
 └── Agent

Infrastructure
 ├── StoreClient
 └── Database

CLI
```

The next devlog will describe the development of the first software units, based on some of the designs presented earlier.
