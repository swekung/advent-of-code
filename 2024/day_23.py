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
import regex as re

raw = aoc_helper.fetch(23, 2024)


def parse_raw(raw: str):
    G = nx.Graph()
    for row in raw.splitlines():
        nodes = re.findall(r"[a-z]+", row)
        for node in nodes:
            G.add_node(node)
        G.add_edge(nodes[0], nodes[1])
    return G

data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = sum([1 if len(c) == 3 and any(n.startswith( 't' ) for n in c ) else 0 for c in list(nx.enumerate_all_cliques(data))])
    return score



aoc_helper.lazy_test(day=23, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    cs = ",".join(sorted(sorted(list(nx.enumerate_all_cliques(data)), key=lambda x: len(x))[-1]))
    return cs


aoc_helper.lazy_test(day=23, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=23, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=23, year=2024, solution=part_two, data=data)
