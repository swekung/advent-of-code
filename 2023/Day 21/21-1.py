from functools import cache
import numpy as np
import sys
import time
import re
from collections import defaultdict, Counter, deque
import heapq
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    plots = {}
    start = (0, 0)
    for (i, row) in enumerate(text):
        for (j, col) in enumerate(row):
            if col == ".":
                plots[(i, j)] = "."
            elif col == "S":
                start = (i, j)
                plots[(i, j)] = "."
    return plots, start

def getAdj(plots, curr):
    i = curr[0]
    j = curr[1]
    out = []
    if (i-1,j) in plots:
        if plots[(i-1,j)] == ".":
            out.append((i-1,j))
    if (i+1,j) in plots:
        if plots[(i+1,j)] == ".":
            out.append((i+1,j))
    if (i,j-1) in plots:
        if plots[(i,j-1)] == ".":
            out.append((i,j-1))
    if (i,j+1) in plots:
        if plots[(i,j+1)] == ".":
            out.append((i,j+1))
    return out

def solve(plots, start):
    curr = [start]
    for i in range(64):
        newCurr = []
        for plot in curr:
            adj = getAdj(plots, plot)
            newCurr += adj
            for plot in adj:
                plots[plot] = "O"
        for plot in curr:
            plots[plot] = "."
        print(len(newCurr))
        curr = newCurr
        sum = 0
        for key in plots:
            if plots[key] == "O":
                sum += 1
    
    return sum

def __main__():
    file = "2023\\Day 21\\input.txt"
    plots, start = readFile(file)
    print(solve(plots, start))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))