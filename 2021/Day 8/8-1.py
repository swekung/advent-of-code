import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append((line.rstrip('\n').split("|")))
    text.close()
    return out

def solve(arr):
    appear = 0
    for row in arr:
        for string in row[1].split():
            length = len(string)
            if length == 2:
                appear += 1
            elif length == 3:
                appear += 1
            elif length == 7:
                appear += 1
            elif length == 4:
                appear += 1
    return appear

def __main__():
    file = "Day 8\input.txt"
    arr = readFile(file)
    sum = solve(arr)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))