from functools import reduce
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
        input = reduce(lambda a, kv: a.replace(*kv), DIGIT_NAMES.items(), input)
        first = next(x for x in input if DIGITS.get(x, None))
        second = next(x for x in reversed(input) if DIGITS.get(x, None))
    else:
        first = next(x for x in input if x.isdigit())
        second = next(x for x in reversed(input) if x.isdigit())
    return int(first + second)


def compute_sum(input: List[int]) -> int:
    return sum(input)


def solve_1(input: List[str]) -> int:
    tmp = [extract_numbers_from_line(val, include_words=False) for val in input]
    return compute_sum(tmp)


def solve_2(input: List[str]) -> int:
    tmp = [extract_numbers_from_line(val, include_words=True) for val in input]
    return compute_sum(tmp)


def main():
    with open(f"{INPUT_DIR}/1_1_input.txt") as f:
        x = f.readlines()
        print(solve_1(x))


if __name__ == "__main__":
    main()
