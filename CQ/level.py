from board import Board,Alliance
class Level():
    def __init__(self, name, enemy_board, allies_board, list_of_allies):
        self.name = name
        self.enemy_board = enemy_board
        self.allies_board = allies_board
        self.list_of_allies = list_of_allies
        
    def display(self):
        print('\n')
        print(f"---------- Level: {self.name} ----------")
        print('\n')
        print(self.enemy_board.to_string())
        print('\n')
        print(self.allies_board.to_string())
        print('\n')
