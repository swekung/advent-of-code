from collections import Counter, defaultdict, deque

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)
import regex as re
import numpy as np
from itertools import permutations
from functools import cache
from typing import List, Dict, Tuple, Set, Optional

raw = aoc_helper.fetch(21, 2024)


def parse_raw(raw: str):
    return raw.splitlines()


data = parse_raw(raw)

keypad = {"A": (2, 0), "0": (1, 0), "1": (0, 1), "2": (1, 1), "3": (2, 1), "4": (0, 2), "5": (1, 2), "6": (2, 2), "7": (0, 3), "8": (1, 3), "9": (2, 3)}
arrs = {"<": (0, 0), "v": (1, 0), "^": (2, 0), ">": (1, 1), "A": (2, 1)}
dirs = {"<": (-1, 0), "v": (0, -1), "^": (0, 1), ">": (1, 0)}



def sequence_to_moveset(start, end, avoid=np.array([0, 0])) -> List[str]:
    delta = end - start
    moves = []
    
    dx = delta[0]
    dy = delta[1]
    if dx < 0:
        moves.extend(['<'] * abs(dx))
    else:
        moves.extend(['>'] * dx)

    if dy < 0:
        moves.extend(['^'] * abs(dy))
    else:
        moves.extend(['v'] * dy)

    
    valid_sequences = []
    for p in set(permutations(moves)):
        positions = [start]
        valid = True
        for move in p:
            next_pos = positions[-1] + dirs[move]
            if np.array_equal(next_pos, avoid):
                valid = False
                break
            positions.append(next_pos)
        if valid:
            valid_sequences.append(''.join(p) + 'a')
    
    return valid_sequences if valid_sequences else ['a']

@cache
def min_length(sequence: str, limit: int = 2, depth: int = 0) -> int:
    avoid = np.array([3, 0]) if depth == 0 else np.array([0, 0])
    positions = keypad if depth == 0 else arrs
    current = positions["A"]
    
    total_length = 0
    for char in sequence:
        next_pos = positions[char]
        movesets = sequence_to_moveset(current, next_pos, avoid)
        
        if depth >= limit:
            total_length += len(min(movesets, key=len))
        else:
            min_moves = float('inf')
            for moveset in movesets:
                try:
                    length = min_length(moveset, limit, depth + 1)
                    min_moves = min(min_moves, length)
                except RecursionError:
                    continue
            if min_moves == float('inf'):
                total_length += len(min(movesets, key=len))
            else:
                total_length += min_moves
        
        current = next_pos
    
    return total_length


def calc_score(length, num):
    num = extract_ints("".join(num))
    return length * int(num[0])


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = 0

    for line in data:
        seq = []
        length = min_length(line, limit=2)
        score += calc_score(length, line)
    return score


aoc_helper.lazy_test(day=21, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0

    for line in data:
        seq = []
        length = min_length(line, limit=25)
        score += calc_score(length, line)
    return score


aoc_helper.lazy_test(day=21, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=21, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=21, year=2024, solution=part_two, data=data)
