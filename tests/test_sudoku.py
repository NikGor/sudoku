import pytest

from src.main import *
from collections import Counter


@pytest.fixture
def solution():
    with open('tests/fixtures/light') as f:  # open the file with the sudoku
        return [list(line.strip()) for line in f.readlines()]


def test_is_solved(solution):
    assert [x for x in solution if '*' in x] == []


def test_is_correct(solution):
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            quadrant = get_quadrant(i, j, solution)
            row = solution[i]
            column = list(zip(*solution))[j]
            assert Counter(quadrant)[solution[i][j]] == 1
            assert Counter(row)[solution[i][j]] == 1
            assert Counter(column)[solution[i][j]] == 1
