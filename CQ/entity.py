from abc import ABC, abstractmethod
import random

class Entity:
    def __init__(self, name, symbol, hp, damage):
        self.id= random.randint(1,9999999)
        self.name=name
        self.symbol=symbol
        self.hp=hp
        self.damage=damage
    

class Wall(Entity):
    def __init__(self):
        name="Wall"
        symbol="I"
        hp= 50
        damage= 0
        super().__init__(name, symbol, hp, damage)