import re
from typing import List, Set

from aoc import INPUT_DIR


def remove_prefix(s: str) -> str:
    return re.sub(r"Card\s+\d+: ", "", s)


def split_games(line: str) -> List[str]:
    s = line.strip().split("|")
    return list(map(str.strip, s))


def split_numbers(num_string: str) -> List[int]:
    s = num_string.split()
    return list(map(int, s))


def get_intersection(line: List[Set[int]]) -> Set[int]:
    [l, r] = line
    return l & r


def calculate_score(length: int) -> int:
    if length < 2:
        return length
    else:
        return 2 ** (length - 1)


def solve_1(input: List[str]) -> int:
    s = list(map(remove_prefix, input))
    ss = list(map(split_games, s))
    sss = [list(map(set, map(split_numbers, line))) for line in ss]
    ssss = list(map(get_intersection, sss))
    sssss = list(map(len, ssss))
    ssssss = list(map(calculate_score, sssss))
    return sum(ssssss)


def solve_2(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/4_1_input.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
