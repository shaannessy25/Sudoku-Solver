''' 
This file will solve any sudoku by puzzle using the backtracking algorithm
 
 Rules:
 1. Each column must have exactly the numbers 1-9
 2. Each row must have exactly the numbers 1-9
 3. Each box must have exactly the numbers 1-9

 Edge Cases:
 1. User could enter zero

 Algorithm:
1. Find empty space
2. Attempt to place a number between 1-9 
3. Check to see if that digit is valid
4. 
    a. If number is valid repeat steps
    b. If it is not valid reset squeare and go to step 3
5. Once the board is full display that the sudoku puzzle is solved

'''



board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0], 
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0], 
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0], 
]

def create_board(board): 
    ''' This method will create the board '''
    # TODO: Display a sudoku board in 
  