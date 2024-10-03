from board import  Board
from board import Alliance
from ally import Barbarian,Archer
from enemy import Cannon, ArcherTower
from level import Level
        

barbarian= Barbarian()
archer= Archer()

cannon= Cannon()
archer_tower= ArcherTower()

enemy_board=Board(3,3,Alliance.ENEMY)

enemy_troops_map={
    "Cannon": 2,
    "Archer Tower": 2
}
enemy_board.populate_board(enemy_troops_map)

# original
# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

# reversed
# [2][0] [2][1] [2][2]
# [1][0] [1][1] [1][2]
# [0][0] [0][1] [0][2]

allies_board=Board(3,3,Alliance.ALLY)

allies_troops_map={
    "Barbarian":5,
    "Archer": 6
    }

allies_board.populate_board(allies_troops_map)

level = Level("Forests (1)", enemy_board, allies_board, {"Barbarian":5, "Archer": 6})
level.display()

def print_stats(ally, enemy):
    print('----------------------------------------------------------------')
    print('\n')
    ally.to_string()
    print('\n')
    enemy.to_string()
    print('\n')
    print('----------------------------------------------------------------')

