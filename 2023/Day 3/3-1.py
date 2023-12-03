import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for line in text:
        out.append((line.rstrip('\n')))
    return out

# return all elements adjacent to arr[i][j], above bello left right abd diagonal
def getAdjacents(arr, i, j):
    adj = []
    if i > 0:
        adj.append(arr[i-1][j])
        if j > 0:
            adj.append(arr[i-1][j-1])
        if j < len(arr[i]) - 1:
            adj.append(arr[i-1][j+1])
    if i < len(arr) - 1:
        adj.append(arr[i+1][j])
        if j > 0:
            adj.append(arr[i+1][j-1])
        if j < len(arr[i]) - 1:
            adj.append(arr[i+1][j+1])
    if j > 0:
        adj.append(arr[i][j-1])
    if j < len(arr[i]) - 1:
        adj.append(arr[i][j+1])
    return adj


def solve(arr):
    sum = 0
    subsum = ""
    adj = False
    for (i, line) in enumerate(arr):
        if adj:
            sum += int(subsum)
        subsum = ""
        adj = False
        for (j, char) in enumerate(line):
            if str.isdigit(char):
                subsum += char
                adjacents = getAdjacents(arr, i, j)
                for elem in adjacents:
                    if not elem == "." and not str.isdigit(elem):
                        adj = True
            else:
                if adj:
                    sum += int(subsum)
                subsum = ""
                adj = False
    
    return sum


def __main__():
    file = "2023\\Day 3\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))