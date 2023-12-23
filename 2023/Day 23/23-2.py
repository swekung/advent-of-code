from functools import cache
import numpy as np
import sys
import time
import networkx as nx
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    nodes = {}
    for (i, row) in enumerate(text):
        for (j, col) in enumerate(row):
            if col in [".", "<", ">", "^", "v"]:
                nodes[(i, j)] = [col, []]
    source, target = None, None
    for (i, j) in nodes:
        if source == None:
            source = (i,j)
        target = (i, j)
        if (i-1,j) in nodes:
            nodes[(i, j)][1].append((i-1,j))
        if (i,j-1) in nodes:
            nodes[(i, j)][1].append((i,j-1))
    return nodes, source, target

def solve(nodes, source, dest):
    G = nx.Graph()
    for id in nodes:
        G.add_node(id)
    for id in nodes:
        for target in nodes[id][1]:
            G.add_edge(id, target)
    paths = nx.all_simple_paths(G, source, dest)
    max = 0
    for path in paths:
        if len(path) > max:
            max = len(path)
    return max - 1

def __main__():
    file = "2023\\Day 23\\input.txt"
    nodes, source, dest = readFile(file)
    print(solve(nodes, source, dest))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))