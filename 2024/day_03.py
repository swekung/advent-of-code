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

raw = aoc_helper.fetch(3, 2024)


def parse_raw(raw: str):
    out = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", raw)
    return out


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sum = 0
    for row in data:
        if row[0] is not "":
            sum += int(re.findall(r"\d+", row)[0]) * int(re.findall(r"\d+", row)[1])
    return sum


aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    on = True
    sum  = 0
    for row in data:
        if row[1] is not "":
            on = False
        if row[2] is not "":
            on = True
        if row[0] is not "" and on:
            sum += int(re.findall(r"\d+", row[0])[0]) * int(re.findall(r"\d+", row[0])[1])
    return sum


aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
