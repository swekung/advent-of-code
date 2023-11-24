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
    out = np.array(out, dtype=np.int32)
    return out

def solve(arr):
    arr = arr - np.median(arr)
    arr = np.abs(arr)
    sum = np.sum(arr)
    return sum

def __main__():
    file = "Day 7\input.txt"
    arr = readFile(file)
    sum = solve(arr)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))