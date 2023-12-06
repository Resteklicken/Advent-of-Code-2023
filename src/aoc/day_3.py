import re
from typing import List, Tuple

from aoc import INPUT_DIR


def extract_numbers(line: str) -> List[Tuple[str, int, int]]:
    return [(m.group(), m.start(), m.end()) for m in re.finditer(r"(\d+)", line)]


def check_for_symbols(line: str, start: int, end: int) -> bool:
    start = start - 1 if start > 0 else start
    end = end + 1 if end < len(line) - 1 else end
    return bool(re.search(r"[^\d\.]", line[start:end]))


def is_adjacent_to_symbol(
    schematic: List[str], line_number: int, match: Tuple[str, int, int]
) -> bool:
    adjacent = False
    if line_number > 0:
        adjacent = adjacent or check_for_symbols(
            line=schematic[line_number - 1], start=match[1], end=match[2]
        )
    if line_number < len(schematic) - 1:
        adjacent = adjacent or check_for_symbols(
            line=schematic[line_number + 1], start=match[1], end=match[2]
        )
    adjacent = adjacent or check_for_symbols(
        line=schematic[line_number], start=match[1], end=match[2]
    )
    return adjacent


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
