from typing import List

from aoc import INPUT_DIR


def solve_1(input: List[str]) -> int:
    return 0


def main():
    with open(f"{INPUT_DIR}/2_1_input.txt") as f:
        x = f.readlines()
        print(solve_1(x))


if __name__ == "__main__":
    main()
