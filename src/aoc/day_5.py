import re
import sys
from concurrent.futures import Future, ThreadPoolExecutor
from typing import List, Tuple

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
    # Credit to /u/zuleyorker for this version
    for dst, src, rlen in mapping:
        if src <= seed < src + rlen:
            return dst + (seed - src)
    return seed


def find_location(seed: int, mappings: List[List[List[int]]]) -> Tuple[int, int]:
    cur = seed
    for mapping in mappings:
        cur = resolve_next_mapping(cur, mapping)
    return (seed, cur)


def get_lowest_element(future_list: list[Future[Tuple[int, int]]]) -> int:
    resolved_tuples = [future.result() for future in future_list]
    min_element = min(resolved_tuples, key=lambda x: x[1])
    return min_element[1]


def solve_1(input_data: str) -> int:
    seeds, *rest = input_data.split("\n\n")
    seeds = remove_prefix(seeds)
    seeds = split_numbers(seeds)
    mappings = split_blocks(rest)
    with ThreadPoolExecutor(max_workers=len(seeds)) as pool:
        locations = [pool.submit(find_location, seed, mappings) for seed in seeds]
    return get_lowest_element(locations)


def resolve_seed_ranges_for_brute_force(seeds: List[int]) -> List[int]:
    new = []
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i + 1]):
            new.append(seeds[i] + j)
    return sorted(new)


def resolve_seed_ranges(seeds: List[int]) -> List[int]:
    for i in range(0, len(seeds), 2):
        seeds[i + 1] = seeds[i] + seeds[i + 1] - 1
    return sorted(seeds)


def resolve_next_mapping_inverse(seed: int, mapping: List[List[int]]):
    # Credit to /u/zuleyorker for this version
    for dst, src, rlen in mapping:
        if dst <= seed < dst + rlen:
            return src + (seed - dst)
    return seed


def calculate_mapping_endpoints(mapping: List[List[int]]) -> List[Tuple[int, int]]:
    return sum(
        sorted(
            [(d_start, s_start), (d_start + rlen - 1, s_start + rlen - 1)]
            for d_start, s_start, rlen in mapping
        ),
        [],
    )


def invert_mapping(mapping: List[List[int]], params: List[int]):
    map_endpts = calculate_mapping_endpoints(mapping)

    output_src_endpts = sorted(
        [resolve_next_mapping_inverse(param, mapping) for param in params]
    )
    input_src_endpts = sorted(set([x[0] for x in map_endpts]))
    if input_src_endpts[0] > 0:
        input_src_endpts = [0, input_src_endpts[0] - 1] + input_src_endpts
    if input_src_endpts[-1] < sys.maxsize:
        input_src_endpts = input_src_endpts + [input_src_endpts[-1] + 1, sys.maxsize]
    input_endpts = sorted(set(output_src_endpts) | set(input_src_endpts))

    return input_endpts


def solve_2(input_data: str) -> int:
    seeds, *rest = input_data.split("\n\n")
    seeds = remove_prefix(seeds)
    seeds = split_numbers(seeds)
    seeds = resolve_seed_ranges_for_brute_force(seeds)
    mappings = split_blocks(rest)
    with ThreadPoolExecutor(max_workers=len(seeds)) as pool:
        locations = [pool.submit(find_location, seed, mappings) for seed in seeds]
    return get_lowest_element(locations)


def main():
    with open(f"{INPUT_DIR}/5_1_input.txt", "r", encoding="utf-8") as f:
        x = f.read()
        print(f"Part 1: {solve_1(x)}")
        print(f"Part 2: {solve_2(x)}")


if __name__ == "__main__":
    main()
