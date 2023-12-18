from functools import cache
import numpy as np
import sys
import time
import re
from operator import itemgetter
import heapq
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    dir = []
    len = []
    col = []
    for row in text:
        dir.append(re.findall("^\\w", row)[0])
        len.append(re.findall("\\d", row)[0])
        col.append(row.rstrip("\n").split()[2])
    return dir, len, col

def findSize(points, per):
    points = points[::-1]
    a = 0
    for i in range(len(points) - 1):
        a += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
    return (per // 2 + a // 2 +1)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DNS = ['R', 'D', 'L', 'U']

def solve(dirs, lens, colours):
    dug = []
    per = 0
    pos = (0,0)
    dug.append((0, 0))
    for (dir, len, colour) in zip(dirs, lens, colours):
        h = colour.lstrip("(#").rstrip(")")
        dist = int(h[:-1], 16)
        dir = DIRS[int(h[-1])]
        pos = (pos[0] + dir[0] * dist, pos[1] + dir[1] * dist)
        per += dist
        dug.append(pos)
    return findSize(dug, per)

def __main__():
    file = "2023\\Day 18\\input.txt"
    dirs, lens, colours = readFile(file)
    print(solve(dirs, lens, colours))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))