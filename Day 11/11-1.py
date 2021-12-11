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

def increaseAround(arr, coord):
    arr = np.pad(arr, (1,1), 'constant', constant_values=0)
    coord += 1
    x = coord[0]
    y = coord[1]
    for i in range(-1,2):
        for j in range(-1,2):
            if arr[i + x][j + y] == 0 or arr[i + x][j + y] == 10:
                pass
            else:
                arr[i + x][j + y] += 1
    return arr[1:-1, 1:-1]


def solve(arr, steps):
    flashes = 0
    for i in range(steps):
        arr = arr + 1
        while np.isin(10, arr):
            for coord in np.argwhere(arr > 9):
                flashes += 1
                arr[coord[0]][coord[1]] = 0
                arr = increaseAround(arr, coord)
    return flashes

def __main__():
    file = "Day 11\input.txt"
    arr = readFile(file)
    sum = solve(arr, 100)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))