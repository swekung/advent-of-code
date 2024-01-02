from functools import cache
import numpy as np
import sys
import time
from z3 import Int, Solver, sat
from itertools import combinations
import networkx as nx
from networkx.algorithms.community import louvain_communities
import re
from math import prod
import matplotlib as plt
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    G = nx.Graph()
    for row in text:
        src = re.findall("\\w+", row)[0]
        for node in re.findall("\\w+", row)[1:]:
            G.add_edge(src, node, capacity=1)

    return G

def solve(G):
    start = "qdg"
    end = max(nx.shortest_path(G, start).items(), key=lambda x: len(x[1]))[0]
    _, partition = nx.minimum_cut(G, start, end)
    return len(partition[0]) * len(partition[1])


def __main__():
    file = "2023\\Day 25\\input.txt"
    G = readFile(file)
    print(solve(G))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))