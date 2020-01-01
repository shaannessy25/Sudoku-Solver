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

#TODO: Create/Display sudoku board
#TODO: Find an empty cell
#TODO: Find a valid number for cell
#TODO: Use backtracking if number for cell is not valid

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0], 
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0], 
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def create_board(bo): 
    ''' This method will create the board '''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and  j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")



create_board(board)