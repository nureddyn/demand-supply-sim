from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def observe(self):
        pass

    @abstractmethod
    def decide(self):
        pass

    @abstractmethod
    def act(self):
        pass
