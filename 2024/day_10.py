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

from queue import PriorityQueue

raw = aoc_helper.fetch(10, 2024)


def parse_raw(raw: str):
    return [[int(c) for c in line] for line in raw.splitlines()]

data = parse_raw(raw)


def bfs(grid, start, end):
    open_set = deque()
    open_set.append(start)
    came_from = {}
    came_from[start] = None

    while open_set:
        current = open_set.popleft()
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in neighbors(grid, current):
            if neighbor not in came_from:
                open_set.append(neighbor)
                came_from[neighbor] = current

    return None

def neighbors(map, current):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []
    for direction in directions:
        neighbor = (current[0] + direction[0], current[1] + direction[1])
        if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]):
            if map[neighbor[0]][neighbor[1]] == map[current[0]][current[1]] + 1:
                result.append(neighbor)
    return result

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data):
    zeros = []
    nines = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 9:
                nines.append((y, x))
            if data[y][x] == 0:
                zeros.append((y, x))

    score = 0
    for start in zeros:
        head = 0
        for end in nines:
            path = bfs(data, start, end)
            if path:
                head += 1
                score += 1
        print(head)
    return score
                


aoc_helper.lazy_test(day=10, year=2024, parse=parse_raw, solution=part_one)

def dfs(map, current, end, visited):
    if current == end:
        return 1
    visited.add(current)
    path_count = 0
    for neighbor in neighbors(map, current):
        if neighbor not in visited:
            path_count += dfs(neighbor, end, visited)
    visited.remove(current)
    return path_count

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    zeros = []
    nines = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 9:
                nines.append((y, x))
            if data[y][x] == 0:
                zeros.append((y, x))

    score = 0
    for start in zeros:
        head = 0
        for end in nines:
            path = dfs(data, start, end, set())
            if path:
                head += path
                score += path
    return score


aoc_helper.lazy_test(day=10, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2024, solution=part_two, data=data)
