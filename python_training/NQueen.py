def solveNQueens(board, row, n):
    if row == n:
        printSolution(board)
        return True
    
    # Try placing the queen in each column of the current row
    for col in range(n):
        if isSafe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            
            # Recur to place the next queen
            if solveNQueens(board, row + 1, n):
                return True
            
            # If placing queen in current column didn't lead to a solution, remove it (backtrack)
            board[row][col] = 0
    
    # If no column is suitable, return False (trigger backtracking)
    return False

def isSafe(board, row, col, n):
    # Check this column on previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def printSolution(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

# Initialize an empty 4x4 board
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

solveNQueens(board, 0, n)
