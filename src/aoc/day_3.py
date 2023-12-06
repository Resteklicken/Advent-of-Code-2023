import re
from typing import Any, List, Tuple

from aoc import INPUT_DIR


def extract_numbers(line: str) -> List[Tuple[str, int, int]]:
    return [(m.group(), m.start(), m.end()) for m in re.finditer(r"(\d+)", line)]


def solve_1(input: List[str]) -> int:
    return 0


def solve_2(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/3_1_input.txt") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
