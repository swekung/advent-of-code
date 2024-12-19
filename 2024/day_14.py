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
from sympy.ntheory.modular import crt
import numpy as np
from tqdm import tqdm

raw = aoc_helper.fetch(14, 2024)


def parse_raw(raw: str):
    out = []
    max_x, max_y = 0, 0
    for line in raw.splitlines():
        out.append([int(x) for x in re.findall(r"[-]*\d+", line)])
        x = out[-1][0]
        y = out[-1][1]
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return out, max_x, max_y


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    rs, max_x, max_y = data
    if len(rs) < 15:
        max_x = 11
        max_y = 7
        split = ((5), (3, 4))
    else:
        max_x = 101
        max_y = 103
    q1, q2, q3, q4 = [], [], [], []

    for x, y, dx, dy in rs:
        x += dx * 100
        y += dy * 100
        if x < 0:
            x = max_x*100 + x
        x = x % (max_x)
        if y < 0:
            y = max_y*100 + y
        y = y % (max_y)


        if x < max_x // 2 and y < max_y // 2:
            q1.append((x, y))
        elif x > max_x // 2 and y < max_y // 2:
            q2.append((x, y))
        elif x < max_x // 2 and y > max_y // 2:
            q3.append((x, y))
        elif x > max_x // 2 and y > max_y // 2:
            q4.append((x, y))
        
    return len(q1) * len(q2) * len(q3) * len(q4)
        

aoc_helper.lazy_test(day=14, year=2024, parse=parse_raw, solution=part_one)

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_density(rs, max_x, max_y):
    center = (max_x // 2, max_y // 2)
    
    distances = [manhattan_distance(center, (x, y)) for x, y, _, _ in rs]
    return sum(distances)



# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    rs, max_x, max_y = data
    if len(rs) < 15:
        max_x = 11
        max_y = 7
    else:
        max_x = 101
        max_y = 103

    min_density = (0, 1000000000000)

    for j in tqdm(range(10000)):
        for i, (x, y, dx, dy) in enumerate(rs):
            x += dx * 1
            y += dy * 1
            if x < 0:
                x = max_x + x
            rs[i][0] = x % (max_x)
            if y < 0:
                y = max_y + y
            rs[i][1] = y % (max_y)

        density = get_density(rs, max_x, max_y)

        if int(density) < min_density[1]:
            min_density = (j + 1, int(density))


    return min_density[0]




aoc_helper.lazy_test(day=14, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=14, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=14, year=2024, solution=part_two, data=data)
