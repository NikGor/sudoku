#!/usr/bin/env python3
import copy
from src.load_image import process_image
from src.solve import solve_sudoku  # import the function to solve the sudoku
from src.output import smart_print  # import the function to print the sudoku
from src.tools import add_sudoku_solution_to_image
from src.wrappers import timing


def solve(puzzle):
    print('Sudoku:')
    smart_print(puzzle)  # print the sudoku
    print('Solution:')
    solution = solve_sudoku(puzzle)  # solve the sudoku
    smart_print(solution)  # print the solution


def display(puzzle):
    smart_print(puzzle)  # print


@timing
def run():
    image_path = 'Sudoku.png'  # the path to the image
    puzzle = process_image(image_path)  # process the image
    sudoku = copy.deepcopy(puzzle)
    solution = solve_sudoku(sudoku)  # solve the sudoku
    solve(puzzle)  # solve the sudoku
    for row in puzzle:
        print(row)
    add_sudoku_solution_to_image(image_path, puzzle, solution, 'output.png')  # add the solution to the image


def main():
    run()  # run the main function


if __name__ == '__main__':
    main()  # run the main function
