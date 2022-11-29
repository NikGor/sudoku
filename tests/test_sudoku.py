import pytest
from src.main import solve_sudoku, is_solved
from collections import Counter
from src.tools import get_quadrant, normalize_file_name


@pytest.fixture
def task():
    filename = normalize_file_name('tests/fixtures/light') # get the file name
    with open(filename) as f:  # open the file with the sudoku
        return [list(line.strip()) for line in f.readlines()] # return the sudoku


def test_is_solved(task):
    assert is_solved(solve_sudoku(task)) is True  # if there are no empty cells, return True


def test_is_correct(task):
    solution = solve_sudoku(task)
    for i in range(len(solution)):  # check if there are any empty cells
        for j in range(len(solution[0])):
            assert solution[i][j] != '*'
            quadrant = get_quadrant(i, j, solution)  # get the quadrant of the cell
            row = solution[i]  # get the row of the cell
            column = list(zip(*solution))[j]  # get the column of the cell
            assert Counter(quadrant)[solution[i][j]] == 1
            assert Counter(row)[solution[i][j]] == 1
            assert Counter(column)[solution[i][j]] == 1
