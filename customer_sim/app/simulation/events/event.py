from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def execute(self, environment):
        pass

    @abstractmethod
    def next_events(self):
        pass
