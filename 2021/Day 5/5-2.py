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
        x1 = int(line.split(",")[0])
        y1 = int(line.split(",")[1].split()[0])
        x2 = int(line.split()[2].split(",")[0])
        y2 = int(line.split()[2].split(",")[1])
        if x1 == x2:
            if y2 < y1:
                y1temp = y1
                y1 = y2
                y2 = y1temp
            for i in range(y1,y2+1):
                lines[i][x1] += 1
                if lines[i][x1] == 2:
                    crossings += 1
        elif y1 == y2:
            if x2 < x1:
                x1temp = x1
                x1 = x2
                x2 = x1temp
            for i in range(x1,x2+1):
                lines[y1][i] += 1
                if lines[y1][i] == 2:
                    crossings += 1
        else:
            xInc = 1
            yInc = 1
            tempX = []
            tempY = []
            if x2 < x1:
                xInc = -1
                for i in range(x1, x2-1, xInc):
                    tempX.append(i)
            else:
                for i in range(x1, x2+1, xInc):
                    tempX.append(i)
            if y2 < y1:
                yInc = -1
                for i in range(y1, y2-1, yInc):
                    tempY.append(i)
            else:
                for i in range(y1, y2+1, yInc):
                    tempY.append(i)
            for i in range(len(tempX)):
                lines[tempY[i]][tempX[i]] += 1
                if lines[tempY[i]][tempX[i]] == 2:
                    crossings += 1
    return lines, crossings

def __main__():
    file = "Day 5\input.txt"
    arr = readFile(file)
    lines, crossings = solve(arr)
    print(crossings)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))