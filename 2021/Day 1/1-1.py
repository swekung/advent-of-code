import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(int(line.rstrip('\n')))
    text.close()
    return out

def findIncreases(arr):
    times = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            times += 1
    return times

def __main__():
    file = "Day 1\input-1.txt"
    arr = readFile(file)
    times  = findIncreases(arr)
    print(times)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))