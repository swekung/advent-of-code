import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out = (line.rstrip('\n').split(","))
    text.close()
    return out

def solve(arr):
    perDay = np.zeros(9)
    for fish in arr:
        perDay[int(fish)] += 1
    for i in range(256):
        perDay[(i+7)%9] += perDay[i%9]
    return perDay.sum()

def __main__():
    file = "Day 6\input.txt"
    arr = readFile(file)
    arr = solve(arr)
    print(arr)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))