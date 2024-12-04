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

raw = aoc_helper.fetch(4, 2024)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    found = re.findall(r"(?=(XMAS|SAMX))", data)
    grid = [list(line) for line in data.splitlines()]
    transposed_grid = [''.join(row) for row in zip(*grid)]
    for line in transposed_grid:
        found.extend(re.findall(r"(?=(XMAS|SAMX))", line))
    
    diagonal = ''
    for d in range(-len(grid) + 1, len(grid[0])):
        diagonal = ''.join(grid[i][i - d] for i in range(max(d, 0), min(len(grid), len(grid[0]) + d)))
        found.extend(re.findall(r"(?=(XMAS|SAMX))", diagonal))

    for d in range(len(grid) + len(grid[0]) - 1):
        diagonal = ''.join(grid[i][d - i] for i in range(max(0, d - len(grid[0]) + 1), min(len(grid), d + 1)))
        found.extend(re.findall(r"(?=(XMAS|SAMX))", diagonal))

    
    return len(found)


aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    data = data.splitlines()
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            chunk = [data[x][j-1:j+2] for x in range(i-1, i+2)]
            diag1 = ''.join(chunk[k][k] for k in range(3))
            diag2 = ''.join(chunk[k][2-k] for k in range(3))
            if ('MAS' in diag1 or 'SAM' in diag1) and ('MAS' in diag2 or 'SAM' in diag2):
                score += 1
    return score


aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2024, solution=part_two, data=data)
