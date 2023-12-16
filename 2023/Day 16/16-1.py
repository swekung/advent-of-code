from functools import cache
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
        
def score(arr):
    sum = 0
    for h in arr:
        for g in h:
            if g == "#":
                sum += 1
    return sum

def solve(arr, heads):
    prev = 0
    prevH = []
    rep = 0
    visited = [["." for j in h] for h in arr]
    while len(heads) > 0:
        for (i, head) in enumerate(heads):
            dir = head[1]
            x, y = head[0]
            if x < len(arr) and y < len(arr[0]) and x >= 0 and y >= 0:
                visited[x][y] = "#"
            if head in prevH:
                heads.pop(i)
            elif dir == "right":
                if not y == len(arr[0]):
                    if arr[x][y] == ".":
                        heads[i] = ((x, y+1), dir)
                    elif arr[x][y] == "\\":
                        heads[i] = ((x+1, y), "down")
                    elif arr[x][y] == "/":
                        heads[i] = ((x-1, y), "up")
                    elif arr[x][y] == "|":
                        heads[i] = ((x-1, y), "up")
                        heads.append(((x+1, y), "down"))
                    elif  arr[x][y] == "-":
                        heads[i] = ((x, y+1), dir)
                else:
                    heads.pop(i)
            elif dir == "left":
                if not y == -1:
                    if arr[x][y] == ".":
                        heads[i] = ((x, y-1), dir)
                    elif arr[x][y] == "\\":
                        heads[i] = ((x-1, y), "up")
                    elif arr[x][y] == "/":
                        heads[i] = ((x+1, y), "down")
                    elif arr[x][y] == "|":
                        heads[i] = ((x-1, y), "up")
                        heads.append(((x+1, y), "down"))
                    elif  arr[x][y] == "-":
                        heads[i] = ((x, y-1), dir)
                else:
                    heads.pop(i)
            elif dir == "up":
                if not x == -1:
                    if arr[x][y] == ".":
                        heads[i] = ((x-1, y), dir)
                    elif arr[x][y] == "\\":
                        heads[i] = ((x, y-1), "left")
                    elif arr[x][y] == "/":
                        heads[i] = ((x, y+1), "right")
                    elif arr[x][y] == "|":
                        heads[i] = ((x-1, y), "up")
                    elif  arr[x][y] == "-":
                        heads[i] = ((x, y-1), "left")
                        heads.append(((x, y+1), "right"))
                else:
                    heads.pop(i)
            elif dir == "down":
                if not x == len(arr):
                    if arr[x][y] == ".":
                        heads[i] = ((x+1, y), dir)
                    elif arr[x][y] == "\\":
                        heads[i] = ((x, y+1), "right")
                    elif arr[x][y] == "/":
                        heads[i] = ((x, y-1), "left")
                    elif arr[x][y] == "|":
                        heads[i] = ((x+1, y), dir)
                    elif  arr[x][y] == "-":
                        heads[i] = ((x, y+1), "right")
                        heads.append(((x, y-1), "left"))
                else:
                    heads.pop(i)
            prevH.append(head)
        sc = score(visited)
        if sc == prev:
            rep += 1
        else:
            rep = 0
        prev = sc
    return sc

def __main__():
    file = "2023\\Day 16\\input.txt"
    arr = readFile(file)
    heads = [((0, 0), "right")]
    print(solve(arr, heads))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))