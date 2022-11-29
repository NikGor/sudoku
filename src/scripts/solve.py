#!/usr/bin/env python3
import time  # import the time module to measure the time it takes to solve the sudoku
from src.main import solve_sudoku  # import the function to solve the sudoku
from src.output import smart_print  # import the function to print the sudoku


def main():
    start = time.time()  # start the timer
    with open('sudoku.txt') as f:  # open the file with the sudoku
        task = [list(line.strip()) for line in f.readlines()]
    print('Sudoku:')
    smart_print(task)  # print the sudoku
    solution = solve_sudoku(task)  # solve the sudoku
    print('Solution:')
    smart_print(solution)  # print the solution
    end = time.time()  # stop the timer
    print('Elapsed time:', round((end - start) * 1000, 2), 'ms')  # print the time elapsed


if __name__ == '__main__':
    main()  # run the main function
