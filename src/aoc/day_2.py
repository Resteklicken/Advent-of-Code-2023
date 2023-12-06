import json
import re
from functools import reduce
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


def is_game_possible(rounds: List[bool]) -> bool:
    return all(e for e in rounds)


def sum_possible_games(games: List[bool]) -> int:
    score = 0
    for i, game in enumerate(games):
        if game:
            score += i + 1
    return score


def solve_1(input: List[str]) -> int:
    s = [remove_prefix(l) for l in input]
    ss = [split_rounds(l) for l in s]
    sss = [[split_counts(l) for l in line] for line in ss]
    ssss = [[count_ballz(d) for d in g] for g in sss]
    sssss = [[is_round_possible(d) for d in g] for g in ssss]
    ssssss = [is_game_possible(g) for g in sssss]
    return sum_possible_games(ssssss)


def find_min_ballz(games: List[Dict[str, int]]) -> Dict[str, int]:
    red = [d.get("red", 0) for d in games]
    green = [d.get("green", 0) for d in games]
    blue = [d.get("blue", 0) for d in games]

    return {
        "red": max(red),
        "green": max(green),
        "blue": max(blue),
    }


def calculate_powers(games: List[Dict[str, int]]) -> List[int]:
    return [reduce((lambda x, y: x * y), game.values(), 1) for game in games]


def solve_2(input: List[str]) -> int:
    s = [remove_prefix(l) for l in input]
    ss = [split_rounds(l) for l in s]
    sss = [[split_counts(l) for l in line] for line in ss]
    ssss = [[count_ballz(d) for d in g] for g in sss]
    sssss = [find_min_ballz(g) for g in ssss]
    ssssss = calculate_powers(sssss)
    return sum(ssssss)


def main():
    with open(f"{INPUT_DIR}/2_1_input.txt") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
