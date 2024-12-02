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

raw = aoc_helper.fetch(2, 2024)


def parse_raw(raw: str):
    out = []
    for line in raw.splitlines():
        out.append([int(x) for x in line.split()])

    return out


data = parse_raw(raw)

def test_row(row):
    dir = row[1] - row[0]
    for i in range(1,len(row)):
        if not (((row[i] - row[i-1]) * dir > 0) and abs(row[i] - row[i-1]) in [1,2,3]):
           return False
    return True

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = 0
    for line in data:
        if test_row(line):
            score += 1
    return score


                
                



aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    for row in data:
        score += True in [test_row(row[:i] + row[i+1:]) for i in range(len(row))]
    return score


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
