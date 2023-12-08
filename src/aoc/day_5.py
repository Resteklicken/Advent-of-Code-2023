import re
from typing import List

from aoc import INPUT_DIR


def remove_prefix(s: str) -> str:
    return re.sub(r"seeds:\s+", "", s)


def split_numbers(num_string: str) -> List[int]:
    s = num_string.split()
    return list(map(int, s))


def solve_1(input: List[str]) -> int:
    return 0


def solve_2(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/5_1_input.txt", "r", encoding="utf-8") as f:
        seeds = f.readline()
        seeds = remove_prefix(seeds)
        seeds = split_numbers(seeds)
        print(seeds)
        # print(f"Part 1: {solve_1(x)}")
        # print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
