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
import networkx as nkx
from tqdm import tqdm

raw = aoc_helper.fetch(20, 2024)


def parse_raw(raw: str):
    return [list(s) for s in raw.strip().splitlines()]


data = parse_raw(raw)

def get_neighbors(x, y):
    return [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]

def get_far_neighbors(x, y):
    return [(x, y-2), (x+2, y), (x, y+2), (x-2, y)]

def get_farther_neighbors(x, y):
    neighbors = []
    for dx in range(-20, 21):
        for dy in range(-20, 21):
            if abs(dx) + abs(dy) <= 20:
                neighbors.append((x + dx, y + dy))
    return neighbors


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    map = nkx.Graph()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)
            for nx, ny in get_neighbors(x, y):
                if nx < 0 or ny < 0:
                    continue
                if data[ny][nx] == "#":
                    continue
                map.add_edge((x, y), (nx, ny))
    
    path = nkx.shortest_path(map, start, end)
    saved = {}
    score = 0

    for i, (x, y) in enumerate(path):
        neig = get_far_neighbors(x, y)
        for nx, ny in neig:
            if (nx, ny) in path:
                if path.index((nx, ny)) > (i + 2):
                    if (path.index((nx, ny)) - i) - 2 not in saved:
                        saved[(path.index((nx, ny)) - i) - 2] = 1
                    else:
                        saved[(path.index((nx, ny)) - i) - 2] += 1
                    if (path.index((nx, ny)) - i) - 2 >= 100:
                        score += 1
        
    return score
    
    
            


#aoc_helper.lazy_test(day=20, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    map = nkx.Graph()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)
            for nx, ny in get_neighbors(x, y):
                if nx < 0 or ny < 0:
                    continue
                if data[ny][nx] == "#":
                    continue
                map.add_edge((x, y), (nx, ny))
    
    path = nkx.shortest_path(map, start, end)
    saved = {}
    score = 0

    print(len(path))

    for i, (x, y) in tqdm(enumerate(path)):
        neig = get_farther_neighbors(x, y)
        for nx, ny in neig:
            if (nx, ny) in path:
                manhattan = abs(nx - x) + abs(ny - y)
                savedd = path.index((nx, ny)) - i - manhattan
                if savedd >= 100:
                    score += 1
                # if savedd > 0:
                #     if savedd not in saved:
                #         saved[savedd] = 1
                #     else:
                #         saved[savedd] += 1
        
    return score


#aoc_helper.lazy_test(day=20, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=20, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=20, year=2024, solution=part_two, data=data)
