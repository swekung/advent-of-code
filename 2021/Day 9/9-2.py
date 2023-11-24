import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(list(line.rstrip('\n')))
    text.close()
    out = np.array(out, dtype=np.int32)
    return out

def findBasins(arr):
    sum = []
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            up = down = left = right = float('inf')
 
            if i - 1 >= 0:
                up = arr[i - 1][j]
 
            if i + 1 < m:
                down = arr[i + 1][j]
    
            if j - 1 >= 0:
                left = arr[i][j - 1]
    
            if j + 1 < n:
                right = arr[i][j + 1]
 
            if arr[i][j] < min(up, down, left, right):
                sum.append((i,j))
    return sum

def findBasinSize(arr, startCoord, visitedCoords):
    m = len(arr)
    n = len(arr[0])
    up = down = left = right = float('inf')
    i = startCoord[0]
    j = startCoord[1]
    newCoords = []
    if i - 1 >= 0 and not (i-1, j) in visitedCoords and arr[i-1][j] < 9:
        visitedCoords.append((i-1, j))
        newCoords.append((i-1, j))
        newCoords += findBasinSize(arr, (i-1, j), visitedCoords)
    if i + 1 < m and not (i+1, j) in visitedCoords and arr[i+1][j] < 9:
        visitedCoords.append((i+1, j))
        newCoords.append((i+1, j))
        newCoords += findBasinSize(arr, (i+1, j), visitedCoords)
    if j - 1 >= 0 and not (i, j-1) in visitedCoords and arr[i][j-1] < 9:
        visitedCoords.append((i, j-1))
        newCoords.append((i, j-1))
        newCoords += findBasinSize(arr, (i, j-1), visitedCoords)
    if j + 1 < n and not (i, j+1) in visitedCoords and arr[i][j+1] < 9:
        visitedCoords.append((i, j+1))
        newCoords.append((i, j+1))
        newCoords += findBasinSize(arr, (i, j+1), visitedCoords)
    return newCoords

def __main__():
    file = "Day 9\input.txt"
    arr = readFile(file)
    basins = findBasins(arr)
    basinSize = []
    for coords in basins:
        basinSize.append(len(findBasinSize(arr, coords, [])))
    basinSize.sort()
    print(basinSize[-1] * basinSize[-2] * basinSize[-3])


__main__()
print("--- %s seconds ---" % (time.time() - start_time))