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
    return rows, cols

def getGalaxies(arr):
    galaxies = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "#":
                galaxies.append((i, j))

    return galaxies

def solve(galaxies, cols, rows):
    dist1 = 0
    for (i, galaxy) in enumerate(galaxies):
        for (j, gal) in enumerate(galaxies):
            if i < j:
                dist = abs(gal[0] - galaxy[0]) + abs(gal[1] - galaxy[1])
                for col in rows:
                    if gal[1] > galaxy[1]:
                        if col < gal[1] and col > galaxy[1]:
                            dist += 999999
                    else:
                        if col < galaxy[1] and col > gal[1]:
                            dist += 999999
                for row in cols:
                    if gal[0] > galaxy[0]:
                        if row < gal[0] and row > galaxy[0]:
                            dist += 999999
                    else:
                        if row < galaxy[0] and row > gal [0]:
                            dist += 999999
                #print(f'{galaxy} -> {gal}: {dist}')
                dist1 += dist
    return dist1

def __main__():
    file = "2023\\Day 11\\input.txt"
    arr = readFile(file)
    rows, cols = expand(arr)
    galaxies = getGalaxies(arr)
    print(solve(galaxies, rows, cols))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))