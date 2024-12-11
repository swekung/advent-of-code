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
from functools import cache

raw = aoc_helper.fetch(11, 2024)


def parse_raw(raw: str):
    return [int(x) for x in re.findall(r"\d+", raw)]


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    for i in range(25):
        new = []
        for stone in data:
            str_stone = str(stone)
            if stone == 0:
                new.append(1)
            elif len(str_stone) % 2 == 0:
                new.append(int(str_stone[:len(str_stone) // 2]))
                new.append(int(str_stone[len(str_stone) // 2:]))
            else:
                new.append(stone * 2024)
        data = new
    return len(data)


aoc_helper.lazy_test(day=11, year=2024, parse=parse_raw, solution=part_one)

@cache
def count( n, b ):
    if b == 75:
        return 1
    if n == 0:
        return count( 1, b + 1 )
    ns = str( n )
    nl = len( ns )
    if nl & 1 == 0:
        return ( count( int( ns[ : nl // 2 ] ), b + 1 ) +
                 count( int( ns[ nl // 2 : ] ), b + 1 ) )
    return count( n * 2024, b + 1 )


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    for stone in data:
        score += count( stone, 0 )
    return score


aoc_helper.lazy_test(day=11, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2024, solution=part_two, data=data)
