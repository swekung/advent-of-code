import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()

replace = {"|": [[".", "|", "."], [".", "|", "."], [".", "|", "."]],
           "-": [[".", ".", "."], ["-", "-", "-"], [".", ".", "."]],
           "L": [[".", "|", "."], [".", "L", "-"], [".", ".", "."]],
           "J": [[".", "|", "."], ["-", "J", "."], [".", ".", "."]],
           "7": [[".", ".", "."], ["-", "7", "."], [".", "|", "."]],
           "F": [[".", ".", "."], [".", "F", "-"], [".", "|", "."]],
           ".": [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
           "S": [[".", "|", "."], ["-", "S", "-"], [".", "|", "."]]}

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        out.append([*row.rstrip("\n")])
        out[-1] = [(pipe, 0, 0) for pipe in out[-1]]
    outNew = [[0 for j in range(len(out[0]*3))] for i in range(len(out)*3)]
    for i in range(len(out)):
        for j in range(len(out[i])):
            mapI = i * 3
            mapJ = j * 3
            repl = replace[out[i][j][0]]
            for k in range(len(repl)):
                for l in range(len(repl[k])):
                    outNew[mapI + k][mapJ + l] = (repl[k][l], 0, 0)
    for i in range(len(outNew)):
        for j in range(len(outNew[i])):
            if outNew[i][j][0] == "S":
                start = (i, j)
    return outNew, start

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
    s += (getAdjStart(arr, i, j))
    while len(s) != 0:
        curr = s[-1]
        arr[curr[0]][curr[1]] = (arr[curr[0]][curr[1]][0], arr[curr[0]][curr[1]][1] + 1, arr[curr[0]][curr[1]][2])
        next = adj(arr, curr[0], curr[1])
        arr[start[0]][start[1]] = (arr[start[0]][start[1]][0], 0, 0)
        if curr == start:
            s.pop(2)
        elif next != (-1, -1):
            #arr[next[0]][next[1]][1] += (arr[curr[0]][curr[1]][0], arr[curr[0]][curr[1]][1] + 1, arr[curr[0]][curr[1]][2])
            arr[next[0]][next[1]] = (arr[next[0]][next[1]][0], arr[next[0]][next[1]][1], arr[curr[0]][curr[1]][2] + 1)
            s.append(next)
            if next == start and len(s) > 4:
                return arr
        else:
            s.pop()
    return arr

def getAdj(arr, i, j):
    adj = []
    if i > 0:
        adj.append((i-1, j))
    if i < len(arr) - 1:
        adj.append((i+1, j))
    if j < len(arr[0]) - 1:
        adj.append((i, j+1))
    if j > 0:
        adj.append((i, j-1))
    return adj


def enclosed(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][1] == 0 or arr[i][j][0] == "S":
                arr[i][j] = "."
            else:
                arr[i][j] = "L"
    for i in range(len(arr[0])):
        if arr[0][i] == ".":
            arr[0][i] = "O"
        if arr[-1][i] == ".":
            arr[-1][i] = "O"
    for i in range(len(arr)):
        if arr[i][0] == ".":
            arr[i][0] = "O"
        if arr[i][-1] == ".":
            arr[i][-1] = "O"
    arrNew = [[0 for j in range(len(arr[0]))] for i in range(len(arr))]
    first = True
    while arrNew != arr:
        if first:
            first = False
        else:
            arr = [[elem for elem in n] for n in arrNew]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == "O":
                    arrNew[i][j] = "O"
                    for (x, y) in getAdj(arr, i, j):
                        if arr[x][y] == ".":
                            arrNew[x][y] = "O"
                elif arrNew[i][j] != "O":
                    arrNew[i][j] = arr[i][j]
    count = 0
    for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == ".":
                    count += 1
    return arr

def colapse(arr):
    out = [[0 for i in range(int(len(arr[j])/3))] for j in range(int(len(arr)/3))]
    for i in range(0, len(arr), 3):
        for j in range(0, len(arr[i]), 3):
            char = arr[i+1][j+1]
            out[int(i/3)][int(j/3)] = char
    count = 0
    for i in range(len(out)):
        for j in range(len(out[i])):
            if out[i][j] == ".":
                print(f'{i}, {j}')
                count += 1
    for row in out:
        print(row)
    return count


def __main__():
    file = "2023\\Day 10\\input.txt"
    arr, start = readFile(file)
    arr = solve(arr, start)
    print(colapse(enclosed(arr)))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))