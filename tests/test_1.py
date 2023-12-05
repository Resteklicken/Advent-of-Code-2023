import pytest

from aoc import INPUT_DIR
from aoc.day_1 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/1_1_test.txt") as f:
        return f.readlines()


@pytest.fixture
def test_input_2():
    with open(f"{INPUT_DIR}/1_2_test.txt") as f:
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
def test_number_extraction_with_just_numbers(input, expected):
    assert extract_numbers_from_line(input, include_words=False) == expected


def test_solve_1(test_input_1):
    assert solve_1(test_input_1) == 142


@pytest.mark.parametrize(
    "input,expected",
    [
        ["one", "1"],
        ["teight1asfa", "81"],
        ["three16asix", "3166"],
        ["threeight", "38"],
        ["two1nine", "219"],
        ["eightwothree", "823"],
    ],
)
def test_word_to_digit_mapping(input, expected):
    assert map_digit_names(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ["1abc23", 13],
        ["1", 11],
        ["one", 11],
        ["one5", 15],
        ["one1asfa", 11],
        ["three16a", 36],
        ["three16aeight", 38],
        ["two1nine", 29],
        ["eightwothree", 83],
    ],
)
def test_number_extraction_with_spelled_out_numbers(input, expected):
    assert extract_numbers_from_line(input, include_words=True) == expected


def test_solve_2(test_input_2):
    assert solve_2(test_input_2) == 281
