#!/usr/bin/env python3
from src.solve import solve_sudoku  # import the function to solve the sudoku
from src.output import smart_print  # import the function to print the sudoku
from src.cli import parse_args  # import the function to parse the arguments from the command line
from src.tools import normalize_file_name
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
    args = parse_args()  # parse the arguments
    with open(normalize_file_name(args.file)) as f:  # open the file with the sudoku
        puzzle = [list(line.strip()) for line in f.readlines()]
    # solve(puzzle)
    if args.solve:
        solve(puzzle)
    elif args.display:
        display(puzzle)
    else:
        print('No action specified. Use --solve or --display.')


def main():
    run()  # run the main function


if __name__ == '__main__':
    main()  # run the main function