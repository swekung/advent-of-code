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

raw = aoc_helper.fetch(22, 2024)


def parse_raw(raw: str):
    return extract_ints(raw)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = 0
    for num in data:
        for i in range(2000):
            cp = num * 64
            num = num ^ cp
            num = num % 16777216
            cp = int(num / 32)
            num = cp ^ num
            num = num % 16777216
            cp = num * 2048
            num = cp ^ num
            num = num % 16777216
        score += num
    return score




aoc_helper.lazy_test(day=22, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    prices = []
    #data = [123]
    for num in data:
        pr = [(num % 10, 0)]
        pr = [(0, 0)]
        for i in range(2000):
            cp = num * 64
            num = num ^ cp
            num = num % 16777216
            cp = int(num / 32)
            num = cp ^ num
            num = num % 16777216
            cp = num * 2048
            num = cp ^ num
            num = num % 16777216
            pr.append((num % 10, num %10 - pr[-1][0]))
        prices.append(pr)

    max = 0
    checked = set()
    seqs = []

    for pr in prices:
        seen = {}
        for i in range(len(pr) - 4):
            diffs = tuple([pr[i+j][1] for j in range(4)])
            if str(diffs) not in seen:
                seen[str(diffs)] = pr[i+3][0]
            if str(diffs) not in checked:
                checked.add(str(diffs))

        seqs.append(seen)


    for ch in tqdm(checked):
        count = 0
        for seq in seqs:
            if ch in seq:
                count += seq[ch]
        if count > max:
            max = count
        
        
            

    return max


aoc_helper.lazy_test(day=22, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=22, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=22, year=2024, solution=part_two, data=data)
