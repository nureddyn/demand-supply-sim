from .event import Event

class DayStart(Event):
    def execute(event_list):
        return "executing event"

    def next_events():
        return "producing next events"
