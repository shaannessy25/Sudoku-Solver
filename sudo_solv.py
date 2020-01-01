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


def find_empty(bo):
    '''This method will locate and empty cell by checking to see if the cell is 0 or not'''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row and column
    return None

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    '''This method will determine if the number in the cell is valid or not '''
    #Checks to see if row is valid
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #Checks to see if column number is valid
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #Checks to see if nonent number is valid
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True






create_board(board)
solve(board)
print('______________________')
print("Here's your solution!")
create_board(board)