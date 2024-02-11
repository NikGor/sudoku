import os
import copy
from PIL import Image, ImageDraw, ImageFont

VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of possible values


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


def count_possible_values(puzzle, i, j):
    return len(get_possible_values(puzzle, i, j))


def normalize_file_name(arg):  # normalize the file name for the current OS
    return arg.replace('/', os.sep).replace('\\', os.sep)


def get_solution(file_name):
    file_name = normalize_file_name(file_name)
    with open(file_name, 'r') as file:
        puzzle = [list(line.strip()) for line in file.readlines()]
    return solve_sudoku(puzzle)


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


def get_quadrant(i, j, arr):
    x = 3 * (i // 3)
    y = 3 * (j // 3)
    return [arr[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]


def get_possible_values(puzzle, i, j):
    quadrant = get_quadrant(i, j, puzzle)
    row = puzzle[i]
    column = list(zip(*puzzle))[j]
    return set(VALUES) - set(quadrant) - set(row) - set(column)


def add_sudoku_solution_to_image(image_path, original_sudoku, solved_sudoku, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Использование стандартного шрифта PIL

    cell_width = img.width // 9
    cell_height = img.height // 9

    for i in range(9):
        for j in range(9):
            if original_sudoku[i][j] == '*':
                value = str(solved_sudoku[i][j])
                x = j * cell_width + cell_width // 4
                y = i * cell_height + cell_height // 4
                draw.text((x, y), value, fill="black", font=font)

    img.save(output_path)
