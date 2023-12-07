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


def calculate_own_contribution(card_list: List[int], own_index: int) -> int:
    cont = min(card_list[own_index], len(card_list) - 1 - own_index)
    print(f"{own_index=}, {cont=}")
    return cont


def calculate_number_of_cards(card_list: List[int], own_index: int) -> int:
    own_contribution = calculate_own_contribution(card_list, own_index)
    if own_contribution == 0:
        return 1
    total_contribution = own_contribution
    for i in range(own_contribution):
        print(f"{own_index=}: {own_contribution=}, {total_contribution=}")
        total_contribution += calculate_number_of_cards(card_list, own_index + i + 1)
    return total_contribution


def solve_2(input: List[str]) -> int:
    s = list(map(remove_prefix, input))
    ss = list(map(split_games, s))
    sss = [list(map(set, map(split_numbers, line))) for line in ss]
    ssss = list(map(get_intersection, sss))
    sssss = list(map(len, ssss))
    ssssss = [calculate_number_of_cards(sssss, i) for i, _ in enumerate(sssss)]
    return sum(ssssss)


def main():
    with open(f"{INPUT_DIR}/4_1_input.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
