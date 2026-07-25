from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def execute(environment):
        pass

    @abstractmethod
    def next_events():
        pass
