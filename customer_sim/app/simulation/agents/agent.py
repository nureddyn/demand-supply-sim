from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def observe(self, env) -> str:
        pass

    @abstractmethod
    def decide(self, observation):
        pass

    @abstractmethod
    def act(self, observation):
        pass

