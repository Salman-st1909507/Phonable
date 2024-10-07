from entity import Entity
from interfaces import IAttack

class Ally(Entity,IAttack):
    
    def __init__(self, name, symbol, hp, damage):
        super().__init__(name,symbol,hp,damage)

    def attack(self, entity):
        entity.hp-=self.damage
        print(f'{self.name} attacked {entity.name}: {self.damage}')
        
    def die(self, ally):
        if self.hp < 0:
            print(f'{self.name} defeated by {ally.name}')

    def distance(self, row, column):
        
        pass
        
        
    def to_string(self):
        print(f'{self.name}\'s stats ({self.symbol}):\nhp: {self.hp}\ndamag: {self.damage}')


class Barbarian(Ally):
    def __init__(self):
        hp = 100
        damage = 15
        name = "Barbarian"
        symbol = 'B'
        super().__init__(name, symbol, hp, damage) 
    

class Archer(Ally):
    def __init__(self):
        hp = 60
        damage = 10
        name = "Archer"
        symbol = 'A'
        super().__init__(name, symbol, hp, damage) 
    
