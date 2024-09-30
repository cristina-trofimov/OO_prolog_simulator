from abc import ABC, abstractmethod

class Guard(ABC):
    @abstractmethod
    def check(self, context: dict) -> bool:
        pass