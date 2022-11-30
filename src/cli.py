# command line interface
import argparse


def parse_args():  # parse the arguments from the command line and return them
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('file', help='path to the file with the sudoku')
    return parser.parse_args()
