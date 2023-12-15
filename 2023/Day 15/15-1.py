import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.read()
    out = []
    for row in text.split(","):
        out.append([*row.rstrip("\n")])
    return out
        
def getTarget(arr, i, j):
    rocks = 0
    for i in range(i, -1, -1):
        if arr[i][j] == "O":
            rocks += 1
        if arr[i][j] == "#":
            return len(arr) - i - rocks
    return len(arr) - i - rocks + 1

def solve(arr):
    sum = 0
    for set in arr:
        s = 0
        for char in set:
            s += ord(char)
            s *= 17
            s = s % 256
        print(s)
        sum += s
    return sum

def __main__():
    file = "2023\\Day 15\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))