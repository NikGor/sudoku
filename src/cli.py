# command line interface
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Sudoku solver, takes a sudoku as input and returns its solution.')
    parser.add_argument('file path', metavar='file path', type=str, help='path to the file with the sudoku')
    return parser.parse_args()
