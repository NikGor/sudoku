import os
VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of possible values


def get_quadrant(i, j, arr):  # get the quadrant of a cell
    x = 3 * (i // 3)  # get the x coordinate of the top left corner of the quadrant
    y = 3 * (j // 3)  # get the y coordinate of the top left corner of the quadrant
    return [arr[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]  # return the quadrant of a cell


def count_possible_values(task, i, j):  # count the number of possible values in a cell
    quadrant = get_quadrant(i, j, task)  # get the quadrant of the cell
    row = task[i]  # get the row of the cell
    column = list(zip(*task))[j]  # get the column of the cell
    possible_values = set(VALUES) - set(quadrant) - set(row) - set(column)  # get the possible values
    return len(possible_values)  # return the number of possible values


def find_the_best_cell(task):  # find the cell with the least possible values
    min_possible_values = 10  # set the minimum number of possible values to 10
    cell_i = 0  # set the cell's coordinates to 0
    cell_j = 0  # set the cell's coordinates to 0
    values = []  # set the possible values to an empty list
    for i in range(len(task)):  # iterate through the sudoku
        for j in range(len(task[0])):
            if task[i][j] == '*':  # if the cell is empty
                possible_values = set(VALUES) \
                                  - set(get_quadrant(i, j, task)) \
                                  - set(task[i]) \
                                  - set(list(zip(*task))[j])  # get the possible values
                if len(possible_values) < min_possible_values:
                    min_possible_values = len(possible_values)  # update the minimum number of possible values
                    cell_i = i  # update the cell's coordinates
                    cell_j = j  # update the cell's coordinates
                    values = possible_values  # update the possible values
    return cell_i, cell_j, min_possible_values, values  # return the cell's coordinates and the possible values


def normalize_file_name(arg):
    basedir, _ = os.path.split(os.path.abspath(os.getcwd()))
    return os.path.join(basedir, os.path.normpath(arg))
