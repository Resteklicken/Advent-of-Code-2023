from collections import OrderedDict

import pytest

from aoc import INPUT_DIR
from aoc.day_2 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/2_1_test.txt") as f:
        return f.readlines()


def test_remove_prefix():
    s = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ss = "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    assert remove_prefix(s) == ss


def test_split_rounds():
    s = "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ss = [["6 red", "1 blue", "3 green"], ["2 blue", "1 red", "2 green"]]
    assert split_rounds(s) == ss


def test_split_counts():
    s = ["6 red", "1 blue", "3 green"]
    ss = [(6, "red"), (1, "blue"), (3, "green")]
    assert split_counts(s) == ss


def test_count_balls():
    s = [(6, "red"), (1, "blue"), (3, "green"), (8, "blue")]
    assert count_ballz(s) == {"red": 6, "blue": 9, "green": 3}


def test_is_round_possible():
    assert solve_1(
        ["Game 5: 6 red, 1 blue, 3 green, 8 blue; 2 blue, 1 red, 2 green"]
    ) == [
        {"red": 6, "blue": 9, "green": 3},
        {"red": 1, "blue": 2, "green": 2},
    ]
