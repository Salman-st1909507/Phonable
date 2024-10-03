from abc import ABC, abstractmethod

# Interface
class IAttack(ABC):
    @abstractmethod
    def attack(self, entity):
        """
        Allows Entity to Attack
        """
        pass

# Interface
class IDie(ABC):
    @abstractmethod
    def die(self, entity):
        """
        Allows Entity to Die
        """
        pass