#def add(a, b):
#    return a + b

# from .infrastructure.api.user.user_client import UserClient

def main():
    #user = UserClient()
    #params = user.get_params()

    # params = {"num-of-days": 0,}

    event_list = EventList()
    scheduler = Scheduler(event_list)
    simulation = Simulation(scheduler)
    simulation.execute()



if __name__ == "__main__":
    main()
