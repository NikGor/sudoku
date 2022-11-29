from tools import find_the_best_cell, get_quadrant

VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of possible values


# ----- main solution -----

def solve_sudoku(task):
    if is_solved(task):  # if the sudoku is solved, return it
        return task
    cell_i, cell_j, min_possible_values, values = find_the_best_cell(task)  # find the best cell and its possible values
    for value in values:  # try to put a value in the cell
        if is_valid(task, value, cell_i, cell_j):  # if the value is valid, put it in the cell
            task[cell_i][cell_j] = value
            solution = solve_sudoku(task)  # try to solve the sudoku in recursion
            if is_solved(solution):  # if the sudoku is solved, return it
                return solution
            task[cell_i][cell_j] = '*'  # if the sudoku is not solved, remove the value from the cell
    return task


# ----- checks

# check if a value is valid in a cell
def is_valid(task, value, i, j):
    quadrant = get_quadrant(i, j, task)  # get the quadrant of the cell
    row = task[i]  # get the row of the cell
    column = list(zip(*task))[j]  # get the column of the cell
    return not any((value in quadrant, value in row, value in column))  # check if the value is valid


# check if a sudoku is solved
def is_solved(solution):
    for i in range(len(solution)):  # check if there are any empty cells
        for j in range(len(solution[0])):
            if solution[i][j] == '*':  # if there is an empty cell, return False
                return False
    return True  # if there are no empty cells, return True
