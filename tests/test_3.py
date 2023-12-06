import pytest

from aoc import INPUT_DIR
from aoc.day_3 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/3_1_test.txt", "r") as f:
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


def test_is_adjacent_to_symbol():
    assert is_adjacent_to_symbol(
        [
            "467..114..",
            "...*......",
            "..35..633.",
        ],
        line_number=0,
        match=("467", 0, 3),
    )


def test_solve_1(test_input_1):
    assert solve_1(test_input_1) == 4361


def test_extract_gears():
    assert extract_potential_gears("...*...755....$.*.....664.598..") == [3, 16]


@pytest.mark.parametrize(
    "start1,end1,start2,end2,expected",
    [
        (13, 15, 11, 14, True),
        (13, 15, 15, 18, True),
        (13, 15, 1, 4, False),
        (4, 6, 1, 4, True),
    ],
)
def test_range_overlaps(start1, end1, start2, end2, expected):
    assert range_overlaps(start1, end1, start2, end2) == expected


@pytest.mark.parametrize(
    "line,pos,expected",
    [
        (".755..$.*..664.598..", 0, [755]),
        (".755..$.*..664.598..", 2, [755]),
        (".755..$.*..664.598..", 8, []),
        (".755..$.*..664.598..", 5, []),
        (".755..$.*..664.598..", 14, [664, 598]),
        (".664.598..", 5, [598]),
    ],
)
def test_check_for_numbers(line, pos, expected):
    assert check_for_numbers(line, pos) == expected


@pytest.mark.parametrize(
    "line,line_no,pos,expected",
    [
        (["467..114..", "...*......", "..35..633."], 1, 3, (467, 35)),
        (["...$.*....", ".664.598.."], 0, 4, (664, 598)),
        (["467..114..", "....*.....", "..35.633.."], 1, 4, None),
    ],
)
def test_is_gear(line, line_no, pos, expected):
    assert is_gear(line, line_no, pos) == expected


def test_solve_2(test_input_1):
    assert solve_2(test_input_1) == 467835
