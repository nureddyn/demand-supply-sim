from .event import Event
# from utils.

class Arrival(Event):
    def __init__(self, time):
        self.time = time + mock_random_interarrival()
        self.customer = Customer()

    def execute(self, environment):
        # option 1
        self.customer.set_budget(environment.generate_budget())

        store = environment.get_store()
        self.customer.request_products(store)

        # option 2
        #budget = environment.generate_budget()
        #wish_list = 
        #customer = CustomerFactory(customer, )

        return "executing event"

    def next_events():
        return "producing next events"


def mock_random_interarrival():
    pass

