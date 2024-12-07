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

from tqdm import tqdm

raw = aoc_helper.fetch(6, 2024)


def parse_raw(raw: str):
    map = Grid.from_string(raw,cl)
    lines = raw.splitlines()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == "^":
                start = (i,j)
        
    
    return (map, start, (i,j))

def cl(ch):
    if ch == "#":
        return 1
    elif ch == ".":
        return 0
    return 0

data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    map, pos, (i,j) = data
    dir = (-1,0)
    visited = set()
    visited.add(pos)
    while True:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos[0] < 0 or next_pos[0] > i or next_pos[1] < 0 or next_pos[1] > j:
            break
        while map[next_pos[0]][next_pos[1]] == 1:
            dir = (dir[1], -dir[0])  # Rotate 90 degrees clockwise
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        pos = next_pos
        visited.add(pos)
    return len(visited)


aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    map, Opos, (i,j) = data
    
    score = 0

    # find how many patterns matching the given pattern where only one # is missing
    # .#....
    # ....#.
    # #.....
    # ...#..

    for k, row in tqdm(enumerate(map)):
        for l, ch in enumerate(row):
            changed = False
            if ch == 1:
                continue
            else:
                map[k][l] = 1
                changed = True
            
            dir = (-1,0)
            visited = set()
            pos = Opos
            visited.add((pos, dir))
            while True:
                next_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if next_pos[0] < 0 or next_pos[0] > i or next_pos[1] < 0 or next_pos[1] > j:
                    break
                while map[next_pos[0]][next_pos[1]] == 1:
                    dir = (dir[1], -dir[0])  # Rotate 90 degrees clockwise
                    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
                pos = next_pos
                if (pos, dir) in visited:
                    score += 1
                    break
                visited.add((pos, dir))
            if changed:
                map[k][l] = 0
    return score

                


aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2024, solution=part_two, data=data)
