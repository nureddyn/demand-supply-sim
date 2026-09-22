
# This is the simulation's main program
class Scheduler:
    def __init__(self, event_list):
        num_of_days = 0
        # duration in minutes
        DAY_DURATION = 1440
        self.clock = Clock()
        self.event_list = event_list

    def execute(self):
        # for
        pass

    def advance_time(self, new_time):
        self.clock.set_time(new_time)

    def timing_routine(self, environment):
        days_left = self.num_of_days

        while days_left > 0:
            first_event = DayStart
            self.event_list.insert(first_event)
            while event_list:
                event = event_list.extract_min()
                event = event()
		if event.time >= DAY_DURATION:
			break
		self.advance_time(event.time)
		event.execute(environment)
		new_events = event.next_events()
		event_list.insert_many(new_events)
            days_left -= 1

