import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        out.append([*row.rstrip("\n")])
    
    return out
        
def expand(arr):

    cols, rows = [], []
    for i in range(len(arr)):
        if not "#" in arr[i]:
            rows.append(i)
    for i in range(len(arr[0])):
        found = False
        for j in range(len(arr)):
            if arr[j][i] == "#":
                found = True
        if not found:
            cols.append(i)
    for (i, row) in enumerate(rows):
        arr.insert(row+i, ["." for i in range(len(arr[0]))])
    for (i, col) in enumerate(cols):
        for j in range(len(arr)):
            arr[j].insert(col+i, ".")
    return arr

def getGalaxies(arr):
    galaxies = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "#":
                galaxies.append((i, j))

    return galaxies

def solve(galaxies):
    dist = 0
    for (i, galaxy) in enumerate(galaxies):
        for (j, gal) in enumerate(galaxies):
            if i < j:
                #steps = abs(gal[0] - galaxy[0]) + abs(gal[1] - galaxy[1])
                #print(f'{galaxy} -> {gal}: {steps}')
                dist += abs(gal[0] - galaxy[0]) + abs(gal[1] - galaxy[1])
    return dist

def __main__():
    file = "2023\\Day 11\\input.txt"
    arr = readFile(file)
    arr = expand(arr)
    galaxies = getGalaxies(arr)
    print(solve(galaxies))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))