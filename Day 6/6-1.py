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
    for i in range(80):
        for j in range(len(arr)):
           arr[j] = int(arr[j]) - 1
           if  arr[j] == -1:
               arr.append(8)
               arr [j] = 6
    return arr

def __main__():
    file = "Day 6\input.txt"
    arr = readFile(file)
    arr = solve(arr)
    print(len(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))