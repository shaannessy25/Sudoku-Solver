# Sudoku Solver
___
## Mission
This application will correctly solve any sudoku puzzle in an efficient matter. 
 ___
### Rules:
1. Each row, column, and nonet can contain each number 1-9 exactly once.
2. The sum of all numbers in any nonet, row, or column must match the small number printed in its corner. The sum is equal to 45. 
___
 ### Algorithm
1. Find empty space
2. Attempt to place a number between 1-9 
3. Check to see if that digit is valid
4. 
    a. If number is valid repeat steps
    b. If it is not valid reset squeare and go to step 3
5. Once the board is full display that the sudoku puzzle is solved


