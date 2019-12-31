''' 
This file will solve any sudoku puzzle
 
 Rules:
 1. Each column must have exactly the numbers 1-9
 2. Each row must have exactly the numbers 1-9
 3. Each box must have exactly the numbers 1-9


 Edge Cases:
 1. User could enter zero

'''

class Sudoku_Solver():

    def __init__(self):
        self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    def row(self):
        '''This method will check to see if the row has all numbers'''
        # TODO: Check to see if all numbers are filled in the row
        # TODO: 

    def column(self):
        '''This method will check to see if the columnt has all numbers'''
        # TODO: Check to see if all numbers are filled in the row
        # TODO: 


    def box(self):
        '''This method will check to see if the box has all numbers'''
        # TODO: Check to see if all numbers are filled in the row
        # TODO: 


def create_grid(): 
    ''' This method will create a grid '''
    # TODO: Create a grid
    row = Sudoku_Solver.row()
    column = Sudoku_Solver.column() 
    for i in row:
        for j in column:
            return None
    return None



