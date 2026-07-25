from .event import Event

class Arrival(Event):
    def __init__(self, time):
        self.time = time + mock_random_interarrival()
        self.customer = Customer()

    def execute(self, environment):
        self.customer.set_budget(environment.income_distribution())

        store = environment.get_store()
        self.customer.request_products(store)
        return "executing event"

    def next_events():
        return "producing next events"


def mock_random_interarrival():
    pass

