#### General Context

Devlog 002 detailed the process for creating some of the domain’s basic classes: `Customer`, `Money`, and `Product`. In this devlog, we will seek to supplement these classes with other models in the simulation layer, those most closely related to the domain’s processes, namely: the behavior over time of buyer agents in an environment, generating demand.

It has been decided to proceed with development centered on the `Arrival` class, which will represent the event at which a buyer agent begins to “exist” within the set of agents that generate demand in the store. This means that, within the context of `Arrival`, an instance of the agent is created, a randomized function is executed to generate its budget, and the agent is added to the set of agents in `Environment`.

We will attempt to develop the relevant units as generally as possible, following some of the guidelines set forth in Design Log 004, and supplementing them with new designs as development warrants.

### Task 1 — First development of `Event`, `Arrival`, `Agent`, and `CustomerAgent`

###### Process and Decisions:

1. We create the `simulation/` folder, where we will store the designs related to the simulation.

2. We define the abstract class `Event`, declaring the methods `execute` and `next_events`. This establishes that every event will be executed in the causal chain of events, and that each event will causally trigger other events. 

3. The `Arrival` class is defined, inheriting directly from `Event`. `Arrival` is structured as follows:

- Definition of the `execute` method, which will produce instances of `Customer`, `CustomerAgent`, and a value for `budget`, with the three interacting through composition: `CustomerAgent(Customer(budget))`.

- `CustomerAgent` will be inserted into a list representing the agent space of `Environment`. We will define `Environment`, which will be passed as an argument to `execute`,later on, so for now we will assume that it exists and that it has the `agent_space` field and the `seed_budget` method, which randomly generates the `budget` value assigned to the buyer agent.

- The relationship between `Arrival`, `Customer`, and `CustomerAgent` will be a simple dependency, so we import the modules into the `arrival.py` file. This decision is made because we found no reason to pass instances of these classes as arguments to `execute`. On the other hand, `environment` is passed as an argument to `execute` since events are logically and structurally coupled with `environment`, that is, every simulated event must occur within a simulated environment and, in turn, must be able to modify or be influenced by that environment.

4. We define the abstract class `Agent` with the dummy methods `observe`, `decide`, and `act`. Next, we define the class `CustomerAgent`, which inherits directly from `Agent`. In addition, `CustomerAgent` receives a `Customer` instance as an argument in its constructor.
