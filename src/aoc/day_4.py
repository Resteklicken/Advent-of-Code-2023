import re
from typing import List

from aoc import INPUT_DIR


def remove_prefix(s: str) -> str:
    return re.sub(r"Card\s+\d+: ", "", s)




def solve_1(input: List[str]) -> int:
    return 0


def solve_2(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/4_1_input.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
