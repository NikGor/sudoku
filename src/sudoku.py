import time
from collections import Counter
import copy

VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
COLOURS = {0: '\033[0m', 1: '\033[32m', 2: '\033[33m', 3: '\033[31m', 4: '\033[0m', 5: '\033[0m', 6: '\033[0m',
           7: '\033[0m', 8: '\033[0m', 9: '\033[0m'}


# ----- main solution -----

def solve_sudoku(input):
    if is_solved(input):
        return input
    cell_i, cell_j, min_possible_values, values = find_the_best_cell(input)
    for value in values:
        if is_valid(input, value, cell_i, cell_j):
            input[cell_i][cell_j] = value
            solution = solve_sudoku(input)
            if is_solved(solution):
                return solution
            input[cell_i][cell_j] = '*'
    return input


# ----- tools -----

def get_quadrant(i, j, arr):
    x = 3 * (i // 3)
    y = 3 * (j // 3)
    return [arr[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]


def count_possible_values(input, i, j):
    quadrant = get_quadrant(i, j, input)
    row = input[i]
    column = list(zip(*input))[j]
    possible_values = set(VALUES) - set(quadrant) - set(row) - set(column)
    return len(possible_values)


def find_the_best_cell(input):
    min_possible_values = 10
    cell_i = 0
    cell_j = 0
    values = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '*':
                possible_values = set(VALUES) \
                                  - set(get_quadrant(i, j, input)) \
                                  - set(input[i]) \
                                  - set(list(zip(*input))[j])
                if len(possible_values) < min_possible_values:
                    min_possible_values = len(possible_values)
                    cell_i = i
                    cell_j = j
                    values = possible_values
    return cell_i, cell_j, min_possible_values, values


# ----- output -----

def smart_print(input):
    for i in range(9):
        if i % 3 == 0:
            print('-------------------------')
        for j in range(len(input[0])):
            if j % 3 == 0:
                print('|', end=' ')
            if input[i][j] == '*':
                print(f'{COLOURS[count_possible_values(input, i, j)]}{input[i][j]}\033[0m', end=' ')
            else:
                print(f'{input[i][j]}', end=' ')
        print('|')
    print('-------------------------')


# ----- tests -----


def is_valid(input, value, i, j):
    quadrant = get_quadrant(i, j, input)
    row = input[i]
    column = list(zip(*input))[j]
    return not any((value in quadrant, value in row, value in column))


def is_solved(solution):
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            if solution[i][j] == '*':
                return False
    return True


def is_correct(solution):
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            quadrant = get_quadrant(i, j, solution)
            row = solution[i]
            column = list(zip(*solution))[j]
            if Counter(quadrant)[solution[i][j]] > 1 or Counter(row)[solution[i][j]] > 1 or Counter(column)[
                solution[i][j]] > 1:
                return False
    return True


# ----- main -----

start = time.time()
with open('sudoku.txt') as sudoku:
    print('Sudoku:')
    input = [list(line.strip()) for line in sudoku]
smart_print(input)
input_1 = copy.deepcopy(input)
print('Solution:')
smart_print(solve_sudoku(input_1))
end = time.time()
if is_solved(solve_sudoku(input)) and is_correct(solve_sudoku(input)):
    print('Tests passed 100%')
print('Elapsed time:', round((end - start) * 1000, 2), 'ms')
