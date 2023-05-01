'''this is Aaron's code. i used nueralnine's backtracking tutorial to help me with this skill
this tutroial is found on youtube'''

'''this method is used to backtrack all the open cells to see if a number 
that is placed in them is valid and flollows all the rules of sodoku'''
def is_valid(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    corner_row = row - row % 3
    corner_col =col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == num:
                return False

    return True

'''this is the main method  used to solve to soduko puzzle. here the method will 
check the cells to see if they have an empty space or prexisting parameter in them'''
def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col =0
    if grid[row][col]>0:
        return solve(grid, row, col + 1)
    for num in range(1,10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True
        grid[row][col] =0
    return False

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end= " ")
        print()
else:
    print("no solutions bozo")
