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
import networkx as nx
from tqdm import tqdm

raw = aoc_helper.fetch(18, 2024)


def parse_raw(raw: str):
    return [tuple(extract_ints(line)) for line in raw.splitlines()]


data = parse_raw(raw)

def get_open_neighbors(x, y, blocked, size):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in blocked and 0 <= nx < size and 0 <= ny < size:
            yield nx, ny

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    blocked = data[:12 if len(data) < 40 else 1024]
    size = 7 if len(data) < 40 else 71

    graph = nx.DiGraph()
    
    for i in range(size):
        for j in range(size):
            if (i, j) not in blocked:
                graph.add_node((i, j))
                for ni, nj in get_open_neighbors(i, j, blocked, size):
                    graph.add_edge((i, j), (ni, nj))
                
    print(nx.shortest_path(graph, (0, 0), (size - 1, size - 1)))
    return nx.shortest_path_length(graph, (0, 0), (size - 1, size - 1))



aoc_helper.lazy_test(day=18, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):

    size = 7 if len(data) < 40 else 71
    k = 1025
    prev = []

    for l in tqdm(range(1025, len(data))):
        if data[l] in prev:
            graph = nx.DiGraph()

            blocked = data[:k]
            k += 1
        
            for i in range(size):
                for j in range(size):
                    if (i, j) not in blocked:
                        graph.add_node((i, j))
                        for ni, nj in get_open_neighbors(i, j, blocked, size):
                            graph.add_edge((i, j), (ni, nj))
                        
            if not nx.has_path(graph, (0, 0), (size - 1, size - 1)):
                return ",".join(map(str, blocked[-1]))
            else:
                prev = nx.shortest_path(graph, (0, 0), (size - 1, size - 1))

    return nx.shortest_path_length(graph, (0, 0), (size - 1, size - 1))


#aoc_helper.lazy_test(day=18, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=18, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=18, year=2024, solution=part_two, data=data)
