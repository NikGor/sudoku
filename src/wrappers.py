import time

from src.output import smart_print


def timing(function):
    def inner(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print('Elapsed time:', round((end - start) * 1000, 2), 'ms')
        return result
    return inner


def display(function):
    def inner(*args):
        print('Sudoku:')
        smart_print(*args)  # print the sudoku
        print('Solution:')
        result = function(*args)
        smart_print(result)  # print the solution
        return result
    return inner
