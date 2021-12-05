import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append((line.rstrip('\n')))       
    text.close()
    return out

def solve(arr):
    lines = np.zeros((1000,1000))
    crossings  = 0
    for line in arr:
        xInc = 1
        yInc = 1
        x1 = int(line.split(",")[0])
        y1 = int(line.split(",")[1].split()[0])
        x2 = int(line.split()[2].split(",")[0])
        y2 = int(line.split()[2].split(",")[1])
        if x1 == x2:
            if y1 > y2:
                yInc = -1
            for i in range(y1,y2+yInc, yInc):
                lines[i][x1] += 1
                if lines[i][x1] == 2:
                    crossings += 1
        if y1 == y2:
            if x1 > x2:
                xInc = -1
            for i in range(x1,x2+xInc, xInc):
                lines[y1][i] += 1
                if lines[y1][i] == 2:
                    crossings += 1
    return lines, crossings

def __main__():
    file = "Day 5\input.txt"
    arr = readFile(file)
    lines, crossings = solve(arr)
    print(crossings)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))