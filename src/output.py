from src.tools import *

COLOURS = {0: '\033[0m', 1: '\033[32m', 2: '\033[33m', 3: '\033[31m', 4: '\033[0m', 5: '\033[0m', 6: '\033[0m',
           7: '\033[0m', 8: '\033[0m', 9: '\033[0m'}  # colours for the possible values


def smart_print(field):  # print the sudoku with the possible values
    for i in range(9):  # print the sudoku
        if i % 3 == 0:  # print a line between the quadrants
            print('-------------------------')
        for j in range(len(field[0])):  # print the values
            if j % 3 == 0:
                print('|', end=' ')  # print a line between the quadrants
            if field[i][j] == '*':  # if the cell is empty
                print(f'{COLOURS[count_possible_values(field, i, j)]}{field[i][j]}\033[0m', end=' ')  # mark the cell
            else:  # if the cell is not empty, print the value
                print(f'{field[i][j]}', end=' ')  # print the value
        print('|')  # print the end of the line
    print('-------------------------')  # print the end of the sudoku
