# command line interface
import argparse


def parse_args():  # parse the arguments from the command line and return them
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('file', help='path to the file with the sudoku')
    parser.add_argument('-s', '--solve', action='store_true', help='solve the sudoku')
    parser.add_argument('-d', '--display', action='store_true', help='display the sudoku')
    return parser.parse_args()
