import re
from typing import Any, List, Tuple

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
    lines = [extract_numbers(line) for line in input]
    parts = []
    for i, line in enumerate(lines):
        for part in line:
            if is_adjacent_to_symbol(input, i, part):
                parts.append(int(part[0]))
    return sum(parts)


def extract_potential_gears(line: str) -> List[int]:
    return [m.start() for m in re.finditer(r"(\*)", line)]


def range_overlaps(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return end1 >= start2 and end2 >= start1


def check_for_numbers(line: str, pos: int) -> List[int]:
    start = pos - 1 if pos > 0 else pos
    end = pos + 1 if pos < len(line) - 1 else pos
    numbers = [
        (int(m.group()), m.start(), m.end()) for m in re.finditer(r"(\d+)", line)
    ]
    return [num[0] for num in numbers if range_overlaps(num[1], num[2] - 1, start, end)]


def is_gear(schematic: List[str], line_number: int, pos: int) -> Tuple[int, int] | None:
    adjacent_numbers = []
    if line_number > 0:
        adjacent_numbers.extend(
            check_for_numbers(line=schematic[line_number - 1], pos=pos)
        )
    if line_number < len(schematic) - 1:
        adjacent_numbers.extend(
            check_for_numbers(line=schematic[line_number + 1], pos=pos)
        )
    adjacent_numbers.extend(check_for_numbers(line=schematic[line_number], pos=pos))
    ret = tuple(adjacent_numbers) if len(adjacent_numbers) == 2 else None
    return ret


def solve_2(input: List[str]) -> int:
    lines = [extract_potential_gears(line) for line in input]
    gears = []
    for i, line in enumerate(lines):
        for gear in line:
            if g := is_gear(input, i, gear):
                gears.append(g[0] * g[1])
    return sum(gears)


def main():
    with open(f"{INPUT_DIR}/3_1_input.txt", "r") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
