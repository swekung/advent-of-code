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
import networkx as nx

raw = aoc_helper.fetch(16, 2024)


def parse_raw(raw: str):
    out = []
    for line in raw.splitlines():
        out.append(list(line))
    return out


data = parse_raw(raw)


def a_star(start, finish, grid):
    
    def h(node):
        return abs(node[0] - finish[0]) + abs(node[1] - finish[1])
    
    def g(node):
        return abs(node[0] - start[0]) + abs(node[1] - start[1])
    
    def f(node):
        return g(node) + h(node)
    
    def neighbors(node):
        (i, j), (di, dj) = node
        for dk, dl in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + dk, j + dl
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != "#":
                yield (ni, nj), (dk, dl)

    open_set = PriorityQueue()
    open_set.put((f(start), start, (0, 1)))
    came_from = {}
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0

    while not open_set.empty():
        _, current, direction = open_set.get()
        if current == finish:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return g_score[finish]
        
        for neighbor, new_direction in neighbors((current, direction)):
            tentative_g_score = g_score[current] + 1
            if new_direction != direction:
                tentative_g_score += 1000
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.put((tentative_g_score + h(neighbor), neighbor, new_direction))
    return None


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                finish = (i, j)
    
    path = a_star(start, finish, data)
    return path


aoc_helper.lazy_test(day=16, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    graph = nx.DiGraph()

    for i, line in enumerate(data):
        for j, cell in enumerate(line):
            if cell == "#":
                continue
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)

            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                graph.add_node(((i, j), direction))

    for node, (di, dj) in graph.nodes:
        destination = (node[0] + di, node[1] + dj)


        if (destination, direction) in graph.nodes:
            graph.add_edge((node, direction), (destination, direction), weight=1)

        for new_direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            graph.add_edge((node, direction), (node, new_direction), weight=1000)

    for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        graph.add_edge((end, direction), "end", weight=0)

    paths = nx.all_shortest_paths(graph, (start, (0, 1)), "end", weight="weight")
    
    nodes = set()
    for path in paths:
        for node in path:
            if node != "end":
                nodes.add(node[0])

    return len(nodes)

aoc_helper.lazy_test(day=16, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=16, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=16, year=2024, solution=part_two, data=data)
