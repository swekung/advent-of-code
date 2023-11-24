from typing import Counter
import numpy as np
import sys
import time
import networkx as nx
start_time = time.time()


def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out = line.rstrip('\n')
    out = out.split()
    xMin = int(out[2].split("..")[0].split("=")[1])
    xMax = int(out[2].split("..")[1].strip(","))
    yMin = int(out[3].split("..")[0].split("=")[1])
    yMax = int(out[3].split("..")[1].strip(","))
    text.close()
    return xMin, xMax, yMin, yMax

def solve(xMin, xMax, yMin, yMax):
    maxHeight = 0
    for i in range(800):
        iStep = i
        for j in range(800):
            max = 0
            i = iStep
            xCoord = 0
            yCoord = 0
            while xCoord <= xMax and yCoord >= yMax:
                yCoord += i
                if yCoord > max:
                    max = yCoord
                xCoord += j
                i -= 1
                if not j == 0:
                    j -= 1
                if xCoord >= xMin and yCoord >= yMin and xCoord <= xMax and yCoord <= yMax:
                    if max > maxHeight:
                        maxHeight = max
    return maxHeight
    



def __main__():
    file = "Day 17/input.txt"
    xMin, xMax, yMin, Ymax = readFile(file)
    totV = solve(xMin, xMax, yMin, Ymax)
    print(totV)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))