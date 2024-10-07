import random
import uuid
from entity import Wall
from level import Level
from utils import reverse_array
from board import Board, Alliance

from ally import Ally,Barbarian,Archer



def generate_board(rows, cols):
    board=[]
    for row in range(rows):
        board.append([])
        for _ in range(cols):
            board[row].append('.')
    return board
            
# def board_str(board):
#     board_str = ""
    
#     for row in range(len(board)):
#         row_str = ""
        
#         for col in range(len(board[row])):
#             row_str+= f"| {board[row][col]} "
#         row_str+= "|"
        
#         for i in range(len(board[0])*5-2):
#             board_str+="-"
        
#         board_str+="\n"
#         board_str+=f"{row_str}\n"
        
#     for i in range(len(board[0])*5-2):
#             board_str+="-"
            
#     return board_str


def board_str(board):
        board_str = ""
        
        for row in range(len(board)):
            row_str = ""
            
            for col in range(len(board[row])):
            
                if board[row][col] == '.':
                    row_str+= f"| . "
                else:
                    row_str+= f"| {board[row][col].symbol} "
                    
            row_str+= "|"+ f'{row}'
            
            for _ in range(len(board[0])*5-2):
                board_str+="-"
            
            board_str+="\n"
            board_str+=f"{row_str}\n"
            
        for _ in range(len(board[0])*5-2):
                board_str+="-"
                
        return board_str



# print(board_str(board))

# uuid.UUID()
# random.random()
# print(random.randint(1,9999999))
# print(uuid.UUID(""))

# print(reversed([1,2,3,4, 5,6,7,8,9,10,11,12]))
# for i in reversed([1,2,3,4, 5,6,7,8,9,10,11,12]):
#     print(i)
    
    
    
# print(reverse_array([1,2,3,4, 5]))

def is_board_full(board):
    for row in range(len(board.board)):
        for col in range(len(board.board[0])):
            if '.' in board.board[row][col]:
                return False
    return True

def is_row_full(board, row):
    for col in range(len(board.board[row])):
        if '.' in board.board[row][col]:
            return False
    return True

def populate_board(board:Board, troops):

    for troop in troops:
        
        row= 0
        col= random.randint(0,len(board.board[0])-1)
        
        cell= board.board[row][col]
        
        while (not cell == '.'):
            if is_row_full(board, row):
                row= (row+1)%len(board.board[row])
            
            if  is_board_full(board):
                break
            
            col= random.randint(0,len(board.board[0])-1)
            cell= board.board[row][col]
            
        board.board[row][col]= troop.symbol


def summon_troops(troops_map: dict[str, int]):
    troops=[]
    
    for key, value in troops_map.items():
        
        if key == "Barbarian":
            for _ in range(value):
                troops.append(Barbarian())
        if key == "Archer":
            for _ in range(value):
                troops.append(Archer())
    return troops

def rearrange_troops(board:Board):
    
    for row in range(len(board.board)):
        
        for col in range(len(board.board[row])):
            
            if board.board[row][col] == '.':
                
                for i in range(row+1,len(board.board)):
                    
                    if not board.board[i][col] == '.':
                        
                        board.board[row][col] = board.board[i][col]
                        board.board[i][col] = '.'
                        break


allies_board= Board(3,3,Alliance.ALLY)
map= {"Barbarian": 5, "Archer": 6}
allies_board.populate_board(map)

enemies_board= Board(3,3,Alliance.ENEMY)
enimies_map={"Cannon": 2, "Archer Tower": 2}
enemies_board.populate_board(enimies_map)

# walls= [[Wall(),Wall(),Wall()]]
walls= [['.','.','.']]

board= enemies_board.board+walls+allies_board.board

level = Level("Forests (1)", enemies_board, allies_board, {"Barbarian":5, "Archer": 6})
# level.display()

print(board_str(board))


def nearest_entity(target_position,array):
    # target_id = array[4][1].id
    nearest_index = None
    min_distance = float('inf')
    # target_position = None

    # # Find the position of target
    # for i in range(len(array)):
    #     for j in range(len(array[i])):
    #         if not array[i][j] == '.':
    #             if array[i][j].id == target_id:
    #                 target_position = (i, j)
    #                 break

    # # If the target is not found, return None
    # if  target_position == None:
    #     return None

    # Calculate distance from the position 
    for i in range(len(array)):
        for j in range(len(array[i])):
            if not array[i][j] == '.':
                # Calculate Manhattan distance
                distance = abs(target_position[0] - i) + abs(target_position[1] - j)
                # Update nearest index if found closer 1
                if distance < min_distance:
                    min_distance = distance
                    nearest_index = (i, j)

    return nearest_index


nearest_index = nearest_entity((4,1),board[0:4])
print(f"The nearest: {nearest_index}")

