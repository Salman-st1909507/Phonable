from enum import Enum
import random
from utils import reverse_array, shuffle
from ally import Barbarian,Archer

class Alliance(Enum):
    ALLY='ALLY'
    ENEMY='ENEMY'

def generate_board(rows, columns):
    board=[]
    for row in range(rows):
        board.append([])
        for _ in range(columns):
            board[row].append('.')
    return board


class Board():
    def __init__(self, rows, columns, alliance):
        self.board = generate_board(rows, columns)
        self.alliance = alliance
        
    def is_board_full(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if '.' in self.board[row][col]:
                    return False
        return True
    
    def is_row_full(self, row):
        for col in range(len(self.board[row])):
            if '.' in self.board[row][col]:
                return False
        return True

    def summon_troops(self, troops_map: dict[str, int]):
        troops=[]
        
        for key, value in troops_map.items():
            
            if key == "Barbarian":
                for _ in range(value):
                    troops.append(Barbarian())
            if key == "Archer":
                for _ in range(value):
                    troops.append(Archer())
                    
        return troops

    def board_str(self):
        board_str = ""
        
        for row in range(len(self.board)):
            row_str = ""
            
            for col in range(len(self.board[row])):
                row_str+= f"| {self.board[row][col]} "
            row_str+= "|"
            
            for _ in range(len(self.board[0])*5-2):
                board_str+="-"
            
            board_str+="\n"
            board_str+=f"{row_str}\n"
            
        for _ in range(len(self.board[0])*5-2):
                board_str+="-"
                
        return board_str

    def rearrange_troops(self):
    
        for row in range(len(self.board)):
            
            for col in range(len(self.board[row])):
                
                if self.board[row][col] == '.':
                    
                    for i in range(row+1,len(self.board)):
                        
                        if not self.board[i][col] == '.':
                            
                            self.board[row][col] = self.board[i][col]
                            self.board[i][col] = '.'
                            break
                        
    def populate_board(self, troops):

        for troop in shuffle(troops):
            
            row= 0
            col= random.randint(0,len(self.board[0])-1)
            
            cell= self.board[row][col]
            
            while (not cell == '.'):
                
                if self.is_row_full(row):
                    row= (row+1)%len(self.board[row])
                
                if  self.is_board_full():
                    break
                
                col= random.randint(0,len(self.board[0])-1)
                cell= self.board[row][col]
                
            self.board[row][col]= troop.symbol
            # self.board[row][col]= troop

    def to_string(self):
        if self.alliance == Alliance.ENEMY:
            self.board = reverse_array(self.board)
            return f'{self.alliance.value}\'s Board:\n{self.board_str()}'
        return f'{self.alliance.value}\'s Board:\n{self.board_str()}'

