import os

from src.solve import solve_sudoku

VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of possible values


def get_quadrant(i, j, arr):
    x = 3 * (i // 3)
    y = 3 * (j // 3)
    return [arr[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]


def find_the_best_cell(puzzle):
    cell_i = 0
    cell_j = 0
    min_possible_values = 10
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == '*':
                if count_possible_values(puzzle, i, j) < min_possible_values:
                    cell_i = i
                    cell_j = j
                    min_possible_values = count_possible_values(puzzle, i, j)
    return cell_i, cell_j


def get_possible_values(puzzle, i, j):
    quadrant = get_quadrant(i, j, puzzle)
    row = puzzle[i]
    column = list(zip(*puzzle))[j]
    return set(VALUES) - set(quadrant) - set(row) - set(column)


def count_possible_values(puzzle, i, j):
    return len(get_possible_values(puzzle, i, j))


def normalize_file_name(arg):  # normalize the file name for the current OS
    return arg.replace('/', os.sep).replace('\\', os.sep)


def get_solution(file_name):
    file_name = normalize_file_name(file_name)
    with open(file_name, 'r') as file:
        puzzle = [list(line.strip()) for line in file.readlines()]
    return solve_sudoku(puzzle)