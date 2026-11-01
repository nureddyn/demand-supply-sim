from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def next_events():
        pass
