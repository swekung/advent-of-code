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
        text = f.readlines()*5
    plots = {}
    start = (0, 0)

    for (i, row) in enumerate(text):
        for (j, col) in enumerate(row*5):
            if col == ".":
                plots[(i, j)] = "."
            elif col == "S" and i == 131 * 2 +65:
                start = (i, j)
                plots[(i, j)] = "."
                
    size = (i, j)
    return plots, start, size

# def getAdj(plots, curr, size):
#     i = curr[0]
#     j = curr[1]
#     out = []
#     if (i-1,j) in plots and i-1 >= 0:
#         if plots[(i-1,j)] == ".":
#             out.append((i-1,j))
#     elif (size[0 ],j) in plots and i-1 < 0:
#         if plots[(size[0],j)] == ".":
#             out.append((size[0],j))
#     if (i+1,j) in plots and i+1 <= size[0]:
#         if plots[(i+1,j)] == ".":
#             out.append((i+1,j))
#     elif (0,j) in plots and i+1 > size[0]:
#         if plots[(0,j)] == ".":
#             out.append((0,j))
#     if (i,j-1) in plots and j-1 >= 0:
#         if plots[(i,j-1)] == ".":
#             out.append((i,j-1))
#     elif (i, size[1]) in plots and j-1 < 0:
#         if plots[(i,size[1])] == ".":
#             out.append((i,size[1]))
#     if (i,j+1) in plots and j+1 <= size[1]:
#         if plots[(i,j+1)] == ".":
#             out.append((i,j+1))
#     elif (i, 0) in plots and j+1 > size[1]:
#         if plots[(i, 0)] == ".":
#             out.append((i,0))
#     return out


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

def pr(plots, size):
    out = [[plots[(i,j)] if (i,j) in plots else "#" for j in range(size[1])] for i in range(size[0])]
    for row in out:
        print("".join(row))


def solve(plots, start, size):
    print(26501300/131)
    curr = [start]
    for i in range(65):
        newCurr = []
        for plot in curr:
            adj = getAdj(plots, plot)
            newCurr += adj
            for plot in adj:
                plots[plot] = "O"
        for plot in curr:
            plots[plot] = "."
        curr = newCurr
    print(len(newCurr))
    for i in range(65+131):
        newCurr = []
        for plot in curr:
            adj = getAdj(plots, plot)
            newCurr += adj
            for plot in adj:
                plots[plot] = "O"
        for plot in curr:
            plots[plot] = "."
        curr = newCurr
    print(len(newCurr))
    for i in range(65+131*2):
        newCurr = []
        for plot in curr:
            adj = getAdj(plots, plot)
            newCurr += adj
            for plot in adj:
                plots[plot] = "O"
        for plot in curr:
            plots[plot] = "."
        curr = newCurr
    print(len(newCurr))
    return len(newCurr)

def __main__():
    file = "2023\\Day 21\\input.txt"
    plots, start, size = readFile(file)
    print(solve(plots, start, size))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))