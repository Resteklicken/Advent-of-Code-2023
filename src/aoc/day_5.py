import re
from typing import List

from aoc import INPUT_DIR


def remove_prefix(s: str) -> str:
    return re.sub(r"seeds:\s+", "", s)


def split_numbers(num_string: str) -> List[int]:
    s = num_string.split()
    return list(map(int, s))


def split_blocks(rest: List[str]) -> List[List[List[int]]]:
    blocks = [block.strip().split("\n") for block in rest]
    return [[list(map(int, row.split())) for row in block[1:]] for block in blocks]


def resolve_next_mapping(seed: int, mapping: List[List[int]]):
    for line in mapping:
        dst, src, range_len = line
        for i, num in enumerate(range(src, src + range_len + 1)):
            if num == seed:
                return dst + i
    return seed


def solve_1(input_data: str) -> int:
    seeds, *rest = input_data.split("\n\n")
    seeds = remove_prefix(seeds)
    seeds = split_numbers(seeds)
    mappings = split_blocks(rest)


def solve_2(input_data: str) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/5_1_test.txt", "r", encoding="utf-8") as f:
        x = f.read()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
