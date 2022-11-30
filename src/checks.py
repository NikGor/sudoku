import copy
from src.tools import get_possible_values


def is_valid(puzzle, value, i, j):
    return value in get_possible_values(puzzle, i, j)


def is_solved(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '*':
                return False
    return True


def is_correct(solution):
    for i in range(9):
        for j in range(9):
            tmp = copy.deepcopy(solution)
            tmp[i][j] = '*'
            if not is_valid(tmp, solution[i][j], i, j):
                return False
    return True
