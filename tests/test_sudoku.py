import pytest
import os
from src.solve import solve_sudoku, is_solved
from collections import Counter
from src.tools import get_quadrant, normalize_file_name


@pytest.fixture
def file_list():
  return os.listdir(normalize_file_name('tests/fixtures'))


def test_is_solved(file_list):
  for file in file_list:
    with open(normalize_file_name('tests/fixtures/' + file)) as f:  # open the file with the sudoku
      puzzle = [list(line.strip()) for line in f.readlines()]  # return the sudoku
      assert is_solved(solve_sudoku(
        puzzle)) is True  # if there are no empty cells, return True


def test_is_correct(file_list):
  for file in file_list:
    with open(normalize_file_name('tests/fixtures/' + file)) as f:  # open the file with the sudoku
      puzzle = [list(line.strip()) for line in f.readlines()]  # return the sudoku
      solution = solve_sudoku(puzzle)
      for i in range(len(solution)):  # check if there are any empty cells
        for j in range(len(solution[0])):
          assert solution[i][j] != '*'
          quadrant = get_quadrant(i, j, solution)  # get the quadrant of the cell
          row = solution[i]  # get the row of the cell
          column = list(zip(*solution))[j]  # get the column of the cell
          assert Counter(quadrant)[solution[i][j]] == 1
          assert Counter(row)[solution[i][j]] == 1
          assert Counter(column)[solution[i][j]] == 1
