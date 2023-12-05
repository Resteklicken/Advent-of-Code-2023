import re
from typing import Any, Dict, List, Tuple

from aoc import INPUT_DIR

BALLZ = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def remove_prefix(s: str) -> str:
    return re.sub(r"Game \d+: ", "", s)


def split_rounds(s: str) -> List[List[str]]:
    return [[sss.strip() for sss in ss.split(",")] for ss in s.split(";")]


def split_counts(input: List[str]) -> List[Tuple[int, str]]:
    return [(int(d), s) for g in input for d, s in [g.split(" ")]]


def count_ballz(input: List[Tuple[int, str]]) -> Dict[str, int]:
    d = {"red": 0, "green": 0, "blue": 0}
    for count, color in input:
        d[color] += count
    return d


def is_round_possible(ballz: Dict[str, int]) -> bool:
    return all(ballz[k] <= BALLZ[k] for k in ballz.keys())


def solve_1(input: List[str]) -> int:
    s: List[str] = [remove_prefix(l) for l in input]
    ss = [split_rounds(l) for l in s]
    sss = [split_counts(ll) for l in ss for ll in l]
    ssss = [count_ballz(g) for g in sss]


def main():
    with open(f"{INPUT_DIR}/2_1_input.txt") as f:
        x = f.readlines()
        print(solve_1(x))


if __name__ == "__main__":
    main()
