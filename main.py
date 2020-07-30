from tabulate import tabulate

# A 9x9 matrix which represents our sudoku solver
sudoku_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Display the board
def display_board(sudoku_board):
    print(tabulate(sudoku_board, tablefmt='fancy_grid'))


#Look for an unassigned cell if it exists return row and col values else return False
def empty_cells_exist():
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                return [i, j]
    return False

# Is our choice good or not?
def valid_number_check(num, i, j):
    #Checking vertically
    for row in range(9):
        if sudoku_board[row][j] == num:
            return False

    #Checking horizontally
    for col in range(9):
        if sudoku_board[i][col] == num:
            return False

    #Check in the 3x3 gird / box
    grid_row = (i // 3) * 3
    grid_col = (j // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku_board[grid_row + i][grid_col + j] == num:
                return False

    # Once all tests are passed return true
    return True

# Solver
def solver():
    cells_exist = empty_cells_exist()

    if not cells_exist:
        return True

    i, j = cells_exist[0], cells_exist[1]
    for num in range(1,10):
        if valid_number_check(num, i, j):
            sudoku_board[i][j] = num
            
            #Backtracking (checking the next step)
            if solver():
                return True
            else:
                sudoku_board[i][j] = 0
                
#     False if nothing (1 through 9) yield an "accepted answer"
    return False

display_board(sudoku_board)

if solver():
    display_board(sudoku_board)
else:
    print("no solution available")
