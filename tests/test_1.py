import pytest

from aoc import INPUT_DIR
from aoc.day_1 import *


@pytest.fixture
def test_input():
    with open(f"{INPUT_DIR}/1_1_test.txt") as f:
        return f.readlines()


@pytest.mark.parametrize(
    "input,expected",
    [
        ["1abc2", 12],
        ["1abc23", 13],
        ["abc23", 23],
        ["abc3", 33],
        ["23", 23],
        ["846sd34abc5729", 89],
        ["1", 11],
    ],
)
def test_number_extraction_with_two_numbers(input, expected):
    assert extract_numbers_from_line(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        [[1, 2], 3],
        [[4, 5, 7, 3], 19],
    ],
)
def test_compute_sum(input, expected):
    assert compute_sum(input) == expected


def test_solve_1(test_input):
    assert solve_1(test_input) == 142
