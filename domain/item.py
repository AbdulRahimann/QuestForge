from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def apply(self,character):
        return "apply this items to a character"