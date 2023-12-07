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
