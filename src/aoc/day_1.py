from functools import reduce
import re
from typing import List

from aoc import INPUT_DIR

DIGIT_NAMES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

""" DIGITS = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
} | DIGIT_NAMES """

DIGITS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
} | DIGIT_NAMES


def extract_numbers_from_line(input: str, include_words: bool = False) -> int:
    if include_words:
        input = map_digit_names(input)
        first = input[0]
        second = input[-1]
    else:
        first = next(x for x in input if x.isdigit())
        second = next(x for x in reversed(input) if x.isdigit())
    return int(first + second)


def map_digit_names(input: str) -> str:
    pattern = "|".join(DIGITS.keys())
    matches = re.finditer(f"(?=({pattern}))", input)
    res = "".join([DIGITS[match.group(1)] for match in matches])
    return res


def solve_1(input: List[str]) -> int:
    return sum([extract_numbers_from_line(val, include_words=False) for val in input])


def solve_2(input: List[str]) -> int:
    return sum([extract_numbers_from_line(val, include_words=True) for val in input])


def main():
    with open(f"{INPUT_DIR}/1_1_input.txt") as f:
        x = f.readlines()
        print(solve_1(x))

    with open(f"{INPUT_DIR}/1_1_input.txt") as f:
        x = f.readlines()
        print(solve_2(x))


if __name__ == "__main__":
    main()
