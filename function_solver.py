# Find where the grid is not solved , solved the grid and return True of false depending on the result

def solve(grid):
    # Find the empty cell
    find = find_empty(grid)
    if not find:
        return True # if the grid is solve
    else:
        row, col = find
    # Resolve the grid by using the static solved_grid_
    for i in range(1,6):
       if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0
    return False # if the grid is not solve

# Find one empty cell to solve
def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j  # return the row, col for the empty cell and exit the loop

def valid(grid, num, pos):
    # compare to the actual value
    # solved_grid =[]
    # if grid == grid_1:
    #     solved_grid == solved_grid_1
    if num != solved_grid_1[pos[0]][pos[1]]:
        return False
    return True