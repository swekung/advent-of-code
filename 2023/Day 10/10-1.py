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
        out[-1] = [(pipe, 0, 0) for pipe in out[-1]]
    for i in range(len(out)):
        for j in range(len(out[i])):
            if out[i][j][0] == "S":
                start = (i, j)
    return out, start

def getAdjStart(arr, i, j):
    out = []
    if arr[i-1][j][0] in ["|", "7", "F"]:
        out.append((i-1, j))
    if arr[i][j+1][0] in ["-", "J", "7"]:
        out.append((i, j+1))
    if arr[i+1][j][0] in ["|", "L", "J"]:
        out.append((i+1, j))
    if arr[i][j-1][0] in ["-", "L", "F"]:
        out.append((i, j-1))
    return out

def adj(arr, i, j):
    pipe = arr[i][j][0]
    visits = arr[i][j][1]
    if i > 0:
        up = arr[i-1][j]
    if i < len(arr) - 1:
        down = arr[i+1][j]
    if j < len(arr[0]) - 1:
        right = arr[i][j+1]
    if j > 0:
        left = arr[i][j-1]

    if pipe == "|":
        if up[1] < visits and up[0] in ["|", "7", "F", "S"]:
            return (i-1, j)
        elif down[1] < visits and down[0] in ["|", "L", "J", "S"]:
            return (i+1, j)
    if pipe == "-":
        if right[1] < visits and right[0] in ["-", "J", "7", "S"]:
            return (i, j+1)
        elif left[1] < visits and left[0] in ["-", "L", "F", "S"]:
            return (i, j-1)
    if pipe == "L":
        if up[1] < visits and up[0] in ["|", "7", "F", "S"]:
            return (i-1, j)
        elif right[1] < visits and right[0] in ["-", "J", "7", "S"]:
            return (i, j+1)
    if pipe == "J":
        if up[1] < visits and up[0] in ["|", "7", "F", "S"]:
            return (i-1, j)
        elif left[1] < visits and left[0] in ["-", "L", "F", "S"]:
            return (i, j-1)
    if pipe == "7":
        if left[1] < visits and left[0] in ["-", "L", "F", "S"]:
            return (i, j-1)
        elif down[1] < visits and down[0] in ["|", "L", "J", "S"]:
            return (i+1, j)
    if pipe == "F":
        if right[1] < visits and right[0] in ["-", "J", "7", "S"]:
            return (i, j+1)
        elif down[1] < visits and down[0] in ["|", "L", "J", "S"]:
            return (i+1, j)
    return (-1, -1)
        

def solve(arr, start):
    s = []
    i, j = start
    arr[i][j] = (arr[i][j][0], 1, 0)
    s += getAdjStart(arr, i, j)
    while s[-1] != start:
        curr = s[-1]
        arr[curr[0]][curr[1]] = (arr[curr[0]][curr[1]][0], arr[curr[0]][curr[1]][1] + 1, arr[curr[0]][curr[1]][2])
        next = adj(arr, curr[0], curr[1])
        arr[start[0]][start[1]] = (arr[start[0]][start[1]][0], 0, 0)
        if next != (-1, -1):
            #arr[next[0]][next[1]][1] += (arr[curr[0]][curr[1]][0], arr[curr[0]][curr[1]][1] + 1, arr[curr[0]][curr[1]][2])
            arr[next[0]][next[1]] = (arr[next[0]][next[1]][0], arr[next[0]][next[1]][1], arr[curr[0]][curr[1]][2] + 1)
            s.append(next)
        else:
            s.pop()
    return (arr[s[-1][0]][s[-1][1]][2] + 1) / 2

def __main__():
    file = "2023\\Day 10\\input.txt"
    arr, start = readFile(file)
    print(solve(arr, start))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))