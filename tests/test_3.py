import pytest

from aoc import INPUT_DIR
from aoc.day_3 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/3_1_test.txt") as f:
        return f.readlines()


def test_extract_numbers():
    assert extract_numbers("......755....$.*.....664.598..") == [
        ("755", 6, 9),
        ("664", 21, 24),
        ("598", 25, 28),
    ]

@pytest.mark.parametrize(
    "line,start,end,expected",
    [
        ("...#*......", 0, 3, True),
        ("...*...#...", 2, 8, True),
        ("...*....#..", 1, 1, False),
        ("...*......", 5, 9, False),
    ],
)
def test_check_for_symbols(line, start, end, expected):
    assert check_for_symbols(line, start, end) == expected

