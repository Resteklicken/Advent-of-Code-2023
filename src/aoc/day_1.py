from functools import reduce
from typing import List, Tuple

from aoc import INPUT_DIR


def extract_numbers_from_line(input: str) -> int:
    first = next(x for x in input if x.isdigit())
    second = next(x for x in reversed(input) if x.isdigit())
    return int(first + second)


def compute_sum(input: List[int]) -> int:
    return sum(input)


def solve_1(input: List[str]) -> int:
    tmp = [extract_numbers_from_line(val) for val in input]
    return compute_sum(tmp)


def main():
    with open(f"{INPUT_DIR}/1_1_input.txt") as f:
        x = f.readlines()
        print(solve_1(x))


if __name__ == "__main__":
    main()
