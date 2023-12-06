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
    assert is_round_possible({"red": 0})
    assert is_round_possible({"red": 0, "blue": 0, "green": 0})
    assert is_round_possible({"blue": 9, "green": 3})
    assert not is_round_possible({"red": 13, "blue": 9, "green": 3})
    assert not is_round_possible({"red": 100, "blue": 100, "green": 0})
    assert not is_round_possible({"red": 12, "blue": 14, "green": 15})


def test_solve_1(test_input_1):
    solve_1(test_input_1)
