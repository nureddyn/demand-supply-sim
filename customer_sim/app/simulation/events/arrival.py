from .event import Event
# from utils.

class Arrival(Event):
    def __init__(self, time):
        self.time = time + mock_random_interarrival()

    def execute(self, environment):
        # option 1
        self.customer.set_budget(environment.generate_budget())

        store = environment.get_store()
        self.customer.request_products(store)
        # --------
        budget_value = environment.generate_budget()
        budget = Budget(budget_value)
        customer = Customer(budget)
        # Where is AgentCustomer?
        # Where do agents will be stored? May be pushing the instance to a list in Environment?

        return "executing event"

    def next_events():
        return "producing next events"


def mock_random_interarrival():
    pass

