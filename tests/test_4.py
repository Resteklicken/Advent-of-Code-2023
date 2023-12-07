import pytest

from aoc import INPUT_DIR
from aoc.day_4 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/4_1_test.txt", "r", encoding="utf-8") as f:
        return f.readlines()


def test_remove_prefix():
    assert (
        remove_prefix(
            """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card      2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
"""
        )
        == """
41 48 83 86 17 | 83 86  6 31 17  9 48 53
13 32 20 16 61 | 61 30 68 82 17 32 24 19
"""
    )


def test_split_games():
    assert split_games(" 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == [
        "13 32 20 16 61",
        "61 30 68 82 17 32 24 19",
    ]


def test_split_numbers():
    assert split_numbers("61 30 68 82 17 32 24 19") == [61, 30, 68, 82, 17, 32, 24, 19]


def test_get_intersection():
    assert get_intersection(
        [{61, 30, 68, 82, 17, 32, 24, 19}, {61, 31, 0, 5, 32, 24, 65}]
    ) == {61, 32, 24}


@pytest.mark.parametrize(
    "length,expected", [(5, 16), (4, 8), (3, 4), (2, 2), (1, 1), (0, 0)]
)
def test_calculate_score(length, expected):
    assert calculate_score(length) == expected


def test_solve_1(test_input_1):
    assert solve_1(test_input_1) == 13


@pytest.mark.parametrize(
    "index,expected", [(0, 4), (1, 2), (2, 2), (3, 0), (4, 1), (5, 0)]
)
def test_calculate_own_contribution(index, expected):
    assert calculate_own_contribution([4, 2, 2, 0, 2, 1], index) == expected
