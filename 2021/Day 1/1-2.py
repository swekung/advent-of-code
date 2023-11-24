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
    previousSums = []
    previousSums.append(arr[0])
    previousSums.append(arr[0]+arr[1])
    previousSums.append(arr[0]+arr[1]+arr[2])
    for i in range(2,len(arr)):
        previousSums.append(arr[i-2]+arr[i-1]+arr[i])
        if previousSums[i] > previousSums[i-1]:
            times += 1
    return times

def __main__():
    file = "Day 1\input-1.txt"
    arr = readFile(file)
    times  = findIncreases(arr)
    print(times)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))