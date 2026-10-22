from .event import Event
# from utils.


class Arrival(Event):
    def __init__(self, time):
        self.time = time + mock_random_interarrival()

    def execute(self, environment):
        # event execution modifies the environment by creating a new agent and inserting it into the customer space
        customer_agent = "CustomerAgent()"
        environment.insert_agent_to_space(customer_agent):
        return

    def next_events():
        return "producing next events"


def mock_random_interarrival():
    pass
