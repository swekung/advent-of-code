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
    gal = []
    for row in text:
        if row == "\n":
            out.append(gal)
            gal = []
        else:
            gal.append([*row.rstrip("\n")])
    out.append(gal)
    return out
        


def solve(maps):
    sum = 0
    for map in maps:
        found = False
        
        for i in range(1, len(map)):
            changed = 0
            for (f, s) in zip(map[i], map[i-1]):
                  if not f == s:
                        changed += 1

            j = 1
            while j + i < len(map) and i-j > 0 and changed <= 1:
                for (f, s) in zip(map[i+j], map[i-j-1]):
                    if not f == s:
                        changed += 1
                j += 1
            if changed == 1:
                found = True
                sum += 100*i
        if not found:
            
            for i in range(1, len(map[0])):
                changed = 0
                col1 = [elem[i] for elem in map]
                col2 = [elem[i-1] for elem in map]
                for (f, s) in zip(col1, col2):
                    if not f == s:
                        changed += 1
                if not found:
                    j = 1
                    while j+i < len(map[0]) and i-j > 0 and changed <= 1:
                        row1 = [elem[j+i] for elem in map]
                        row2 = [elem[i-j-1] for elem in map]
                        for (f, s) in zip(row1, row2):
                            if not f == s:
                                changed += 1
                        j += 1
                    if changed == 1:
                        sum += i

    return sum

def __main__():
    file = "2023\\Day 13\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))