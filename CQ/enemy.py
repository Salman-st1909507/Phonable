from entity import Entity
from interfaces import IAttack

class Enemy(Entity, IAttack):
    
    def __init__(self,name,symbol,hp,damage):
        super().__init__(name,symbol,hp,damage)
        
    def attack(self, entity):
        entity.hp-=self.damage
        print(f'{self.name} attacked {entity.name}: {self.damage}')
        
    def die(self, enemy):
        if self.hp > 0:
            print(f'{self.name} defeated by {enemy.name}')
            
    def to_string(self):
        print(f'{self.name}\'s stat ({self.symbol}):\nhp: {self.hp}\ndamag: {self.damage}')
        
        
class Cannon(Enemy):
    def __init__(self):
        hp = 1500
        damage = 60
        name = "Cannon"
        symbol = 'C'
        super().__init__(name, symbol, hp, damage) 
    

class ArcherTower(Enemy):
    def __init__(self):
        hp = 1100
        damage = 40
        name = "Archer Tower"
        symbol = 'T'
        super().__init__(name, symbol, hp, damage) 
    
