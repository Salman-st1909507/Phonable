from abc import ABC, abstractmethod
from enum import Enum
import random
from entity import Entity
from utils import reverse_array, shuffle
from ally import Barbarian,Archer
from enemy import Cannon,ArcherTower

# class EntityFactory(Entity):
#     def __init__(self, entity):
#         entity = entity
#         pass
    
#     def create_entity(self, name, symbol, hp, damage):
#         self.entity
        

# Define a Troop abstract base class (DIP principle)
class Troop(ABC):
    
    @abstractmethod
    def symbol(self):
        pass

# Concrete classes for different troop types
class Barbarian(Troop):
    def symbol(self):
        return "B"

class Archer(Troop):
    def symbol(self):
        return "A"

class Cannon(Troop):
    def symbol(self):
        return "C"

class ArcherTower(Troop):
    def symbol(self):
        return "AT"

# Simple Factory
class EntityFactory:
    def __init__(self):
        self.registry = {
            "Barbarian": Barbarian,
            "Archer": Archer,
            "Cannon": Cannon,
            "Archer Tower": ArcherTower
        }

    def create_troops(self, troops_map):
        """Creates troops based on the provided troops_map (e.g., {"Barbarian": 3, "Archer": 2})."""
        troops = []
        for troop_type, count in troops_map.items():
            if troop_type in self.registry:
                for _ in range(count):
                    troops.append(self.registry[troop_type]())
        return troops


factory = EntityFactory()

# Map of troop types to number of instances needed
troops_map = {
    "Barbarian": 2,
    "Archer": 3,
    "Cannon": 1
}

# Create the requested troops
troops = factory.create_troops(troops_map)

# Now, troops will be a list of instances of Barbarian, Archer, and Cannon
for troop in troops:
    print(troop.symbol())  # Output: B, B, A, A, A, C
