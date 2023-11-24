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

def solve(arr):
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
                sum.append(arr[i][j])
    return np.sum(sum) + len(sum)

def __main__():
    file = "Day 9\input.txt"
    arr = readFile(file)
    sum = solve(arr)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))