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
from tqdm import tqdm
from functools import cache

raw = aoc_helper.fetch(19, 2024)

rs = []

def parse_raw(raw: str):
    raw = raw.split("\n\n")
    global rs

    rs = re.findall(r"[wubrg]+", raw[0])
    t = raw[1].split("\n")
    return t


data = parse_raw(raw)

@cache
def check(s):
    global rs
    if len(s) == 0:
        return True
    for r in rs:
        if s.startswith(r):
            if check(s[len(r):]):
                return True
    return False

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    global rs
    t = data
    s=0
    
    for row in tqdm(t):
        if check(row):
            s += 1
    return s
        

aoc_helper.lazy_test(day=19, year=2024, parse=parse_raw, solution=part_one)

@cache
def count(s):
    global rs
    c = 0
    if len(s) == 0:
        return 1
    for r in rs:
        if s.startswith(r):
            if check(s[len(r):]):
                c += count(s[len(r):])
    return c


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    global rs
    t = data
    s=0
    
    for row in tqdm(t):
        s += count(row)
    return s


#aoc_helper.lazy_test(day=19, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=19, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=19, year=2024, solution=part_two, data=data)
