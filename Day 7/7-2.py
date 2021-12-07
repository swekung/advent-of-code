import numpy as np
import sys
import time
import math
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out = (line.rstrip('\n').split(","))
    text.close()
    out = np.array(out, dtype=np.int64)
    return out

def solve(arr):
    least_cost = 0
    for i in range(max(arr)):
        cost = 0  
        tmpArr = np.abs(arr - i)
        for j in range(len(tmpArr)):
            cost += (tmpArr[j]*(tmpArr[j]+1))/2
        if cost < least_cost or least_cost == 0:
            least_cost = cost
    return least_cost

def solve2(arr):
    arr = (arr*(arr+1))/2
    arr = arr - np.median(arr)
    arr = np.abs(arr)
    sum = np.sum(arr)
    return sum

def __main__():
    file = "Day 7\input.txt"
    arr = readFile(file)
    arr = solve2(arr)
    print(arr)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))