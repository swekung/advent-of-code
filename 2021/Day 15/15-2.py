from typing import Counter
import numpy as np
import sys
import time
import networkx as nx
from itertools import product

start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(list(line.rstrip('\n')))
    text.close()
    out = np.array(out, dtype=np.int16)
    n = len(out)
    #out = np.pad(out, 1, 'constant', constant_values=9)
    newOut = np.zeros((len(out)*5, len(out)*5), dtype=np.int16)
    for row, col in product(range(n*5), range(n*5)):
        newOut[col][row] = (out[col % n][row % n] - 1 + (row//n) + (col//n)) % 9 + 1    
    #out = np.pad(newOut, 1, 'constant', constant_values=9)
    return newOut

def toNetwork(map):
    n = len(map)
    G = nx.grid_2d_graph(n, n, create_using=nx.DiGraph)
    for u, v in G.edges:
        G[u][v]["weight"] = map[v[1]][v[0]]
    return G

def __main__():
    file = "Day 15/input.txt"
    arr = readFile(file)
    G = toNetwork(arr)
    path = nx.astar_path(G, (0,0), (len(arr)-1,len(arr)-1), weight='weight')
    weight = nx.path_weight(G, path, 'weight')
    print(weight)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))