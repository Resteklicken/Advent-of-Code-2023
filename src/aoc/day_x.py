from typing import List

from aoc import INPUT_DIR


def solve_1(input_data: List[str]) -> int:
    return 0


def solve_2(input_data: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/x_1_input.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
