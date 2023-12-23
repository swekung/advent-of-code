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
        if nodes[(i, j)][0] == "<":
            nodes[(i, j)][1].append((i, j-1))
        elif nodes[(i, j)][0] == ">":
            nodes[(i, j)][1].append((i, j+1))
        elif nodes[(i, j)][0] == "^":
            nodes[(i, j)][1].append((i-1, j))
        elif nodes[(i, j)][0] == "v":
            nodes[(i, j)][1].append((i+1, j))
        else:
            if (i+1,j) in nodes:
                if nodes[(i+1, j)][0] not in ["^"]:
                    nodes[(i, j)][1].append((i+1,j))
            if (i-1,j) in nodes:
                if nodes[(i-1, j)][0] not in ["v"]:
                    nodes[(i, j)][1].append((i-1,j))
            if (i,j+1) in nodes:
                if nodes[(i, j+1)][0] not in ["<"]:
                    nodes[(i, j)][1].append((i,j+1))
            if (i,j-1) in nodes:
                if nodes[(i, j-1)][0] not in [">"]:
                    nodes[(i, j)][1].append((i,j-1))
    return nodes, source, target

def solve(nodes, source, dest):
    G = nx.DiGraph()
    for id in nodes:
        G.add_node(id)
    for id in nodes:
        for target in nodes[id][1]:
            G.add_edge(id, target)
    paths = nx.dag_longest_path(G, source, dest)
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