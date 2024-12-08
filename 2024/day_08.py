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

raw = aoc_helper.fetch(8, 2024)


def parse_raw(raw: str):
    locs = {}
    for y, line in enumerate(raw.splitlines()):
        for x, ch in enumerate(line):
            if ch != ".":
                if ch in locs:
                    locs[ch].append((x, y))
                else:
                    locs[ch] = [(x,y)]
    return locs, (x,y)


data = parse_raw(raw)

def are_collinear(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 - x2), (y1 - y2)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    locs, (max_x, max_y) = data
    ref = set()

    for ch, points in locs.items():
        for point in points:
            (x, y) = point
            for p in points:
                if p != point:
                    x_diff, y_diff = dist(point, p)
                    ref_x = x + x_diff
                    ref_y = y + y_diff
                    if 0 <= ref_x <= max_x and 0 <= ref_y <= max_y:
                        ref.add((ref_x, ref_y))
    return len(ref)


aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    locs, (max_x, max_y) = data
    ref = set()

    for ch, points in locs.items():
        for point in points:
            (x, y) = point
            for p in points:
                if p != point:
                    x_diff, y_diff = dist(point, p)
                    in_bounds = True
                    ref_x = x
                    ref_y = y
                    ref.add((ref_x, ref_y))
                    while in_bounds:
                        ref_x += x_diff
                        ref_y += y_diff
                        if 0 <= ref_x <= max_x and 0 <= ref_y <= max_y:
                            ref.add((ref_x, ref_y))
                        else:
                            in_bounds = False
    return len(ref)


aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2024, solution=part_two, data=data)
