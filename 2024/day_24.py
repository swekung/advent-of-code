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
import networkx as nx
from matplotlib import pyplot as plt

raw = aoc_helper.fetch(24, 2024)


def parse_raw(raw: str):
    raw = raw.split("\n\n")
    regs = {}
    gates = []

    for line in raw[0].splitlines():
        reg, val = line.split(": ")
        regs[reg] = int(val)

    for line in raw[1].splitlines():
        gate = line.split()
        gates.append([gate[1], gate[0], gate[2], gate[4]])

    return regs, gates


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    regs, gates = data

    while len(gates) > 0:
        for i, gate in enumerate(gates):
            gate, in1, in2, out = gate
            if in1 not in regs or in2 not in regs:
                continue
            gates.pop(i)
            if gate == "AND":
                regs[out] = regs[in1] & regs[in2]
            elif gate == "OR":
                regs[out] = regs[in1] | regs[in2]
            elif gate == "XOR":
                regs[out] = regs[in1] ^ regs[in2]

    zs = []
    for reg in regs:
        if reg[0] == "z":
            zs.append(reg)
    
    zs.sort(reverse=True)
    z_bin = "".join([str(regs[z]) for z in zs])
    z_bin = int(z_bin, 2)
    return z_bin
    


#aoc_helper.lazy_test(day=24, year=2024, parse=parse_raw, solution=part_one)


def sim_logic(regs, gates):
    gates = gates.copy()
    while len(gates) > 0:
        for i, gate in enumerate(gates):
            gate, in1, in2, out = gate
            if in1 not in regs or in2 not in regs:
                continue
            gates.pop(i)
            if gate == "AND":
                regs[out] = regs[in1] & regs[in2]
            elif gate == "OR":
                regs[out] = regs[in1] | regs[in2]
            elif gate == "XOR":
                regs[out] = regs[in1] ^ regs[in2]

    return regs

def inspect(reg, gates, d=0, lim=3, G=None):
    if d > lim:
        return
    for g in gates:
        if g[3] == reg:
            print(f"{'  ' * d}{g}")
            if G is not None:
                G.add_edge(g[1], g[3])
                G.add_edge(g[2], g[3])
            inspect(g[1], gates, d+1, lim, G)
            inspect(g[2], gates, d+1, lim, G)

    

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    regs, gates = data
    for i in range(len(regs) // 2):
        t_regs = {}
        for reg in regs:
            t_regs[reg] = 0
        y_str = f"y{i:02d}"
        x_str = f"x{i:02d}"
        z_str = f"z{i+1:02d}"
        t_regs[y_str] = 1
        t_regs[x_str] = 1
        reg = sim_logic(t_regs, gates)
        if reg[z_str] != 1:
            G = nx.DiGraph()
            inspect(z_str, gates, lim=6, G=G)

            print(f"Miss: {i}")

    swaps = ["z09", "nnf", "nhs", "z20", "ddn", "kqh", "wrc", "z34"]
    swaps.sort()
    return ",".join(swaps) 



    


#aoc_helper.lazy_test(day=24, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=24, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=24, year=2024, solution=part_two, data=data)
