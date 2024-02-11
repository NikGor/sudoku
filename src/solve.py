from src.tools import is_solved, get_possible_values, find_the_best_cell


def solve_sudoku(puzzle):
    if is_solved(puzzle):  # if the sudoku is solved, return it
        return puzzle
    cell_i, cell_j = find_the_best_cell(puzzle)  # find the "best" cell
    values = get_possible_values(puzzle, cell_i, cell_j)
    while values:
        puzzle[cell_i][cell_j] = values.pop() 
        solution = solve_sudoku(puzzle)  # try to solve the whole sudoku
        if is_solved(solution):  # if the sudoku is solved, return it
            return solution
        puzzle[cell_i][cell_j] = '*'  # if the sudoku is not solved, remove the value from the cell
    return puzzle
