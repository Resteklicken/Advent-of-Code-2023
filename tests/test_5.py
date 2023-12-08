import pytest

from aoc import INPUT_DIR
from aoc.day_5 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/5_1_test.txt", "r", encoding="utf-8") as f:
        return f.read()


def test_split_blocks():
    assert split_blocks(
        [
            "seed-to-soil map:\n50 98 2\n52 50 48",
            "soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15",
            "fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4",
            "water-to-light map:\n88 18 7\n18 25 70",
            "light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13",
            "temperature-to-humidity map:\n0 69 1\n1 0 69",
            "humidity-to-location map:\n60 56 37\n56 93 4",
        ]
    ) == [
        [[50, 98, 2], [52, 50, 48]],
        [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        [[88, 18, 7], [18, 25, 70]],
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [[0, 69, 1], [1, 0, 69]],
        [[60, 56, 37], [56, 93, 4]],
    ]


@pytest.mark.parametrize(
    "seed,mapping,expected",
    [
        (79, [[50, 98, 2], [52, 50, 48]], 81),
        (81, [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 81),
        (81, [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], 81),
        (81, [[88, 18, 7], [18, 25, 70]], 74),
        (74, [[45, 77, 23], [81, 45, 19], [68, 64, 13]], 78),
        (78, [[0, 69, 1], [1, 0, 69]], 78),
        (78, [[60, 56, 37], [56, 93, 4]], 82),
    ],
)
def test_resolve_next_mapping(seed, mapping, expected):
    assert resolve_next_mapping(seed, mapping) == expected


def test_solve_1(test_input_1):
    assert solve_1(test_input_1) == 35
