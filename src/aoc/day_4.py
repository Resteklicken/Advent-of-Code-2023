import re
from typing import List

from aoc import INPUT_DIR


def remove_prefix(s: str) -> str:
    return re.sub(r"Card\s+\d+: ", "", s)


def split_games(line: str) -> List[str]:
    s = line.strip().split("|")
    return list(map(str.strip, s))


def split_numbers(num_string: str) -> List[int]:
    s = num_string.split(" ")
    return list(map(int, s))


def solve_1(input: List[str]) -> int:
    s = list(map(remove_prefix, input))
    ss = list(map(split_games, s))
    sss = [split_numbers(nums) for line in ss for nums in line]


def solve_2(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/4_1_input.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
