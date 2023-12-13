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
            if map[i] == map[i-1] and not found:
                j = 0
                while j + i < len(map) and i-j > 0:
                    if not map[i+j] == map[i-j-1]:
                        break
                    else:
                        j += 1
                if j + i == len(map) or i-j == 0:
                    sum += 100*i
        if not found:
            for i in range(1, len(map[0])):
                if [elem[i] for elem in map] == [elem[i-1] for elem in map] and not found:
                    j = 0
                    while j+i < len(map[0]) and i-j > 0:
                        print([elem[j+i] for elem in map])
                        print([elem[i-j] for elem in map])
                        if not [elem[j+i] for elem in map] == [elem[i-j-1] for elem in map]:
                            break
                        else:
                            j += 1
                    if j+i == len(map[0]) or i-j == 0:
                        sum += i

    return sum

def __main__():
    file = "2023\\Day 13\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))