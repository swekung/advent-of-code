import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for line in text:
        out.append((line.rstrip('\n')))
    return out

# Gets all positions adjacent to arr[i][j], above belo left right and diagonal
def getAdjacentPositions(arr, i, j):
    adj = []
    if i > 0:
        adj.append((i-1, j))
        if j > 0:
            adj.append((i-1, j-1))
        if j < len(arr[i]) - 1:
            adj.append((i-1, j+1))
    if i < len(arr) - 1:
        adj.append((i+1, j))
        if j > 0:
            adj.append((i+1, j-1))
        if j < len(arr[i]) - 1:
            adj.append((i+1, j+1))
    if j > 0:
        adj.append((i, j-1))
    if j < len(arr[i]) - 1:
        adj.append((i, j+1))
    return adj

#Gets a postion in arr and searches left and right for a number
def getNumber(arr, i, j):
    num = arr[i][j]
    right, left = 1, 1
    while str.isdigit(arr[i][j+right]):
        num += arr[i][j+right]
        right += 1
        if j+right >= len(arr[i]):
            break
    while str.isdigit(arr[i][j-left]):
        num = arr[i][j-left] + num
        left += 1
        if j-left < 0:
            break
    return int(num)

def solve(arr):
    sum = 0
    subsum = ""
    adj = False
    for (i, line) in enumerate(arr):
        for (j, char) in enumerate(line):
            if char == "*":
                numbers = []
                adj = getAdjacentPositions(arr, i, j)
                for (k, l) in adj:
                    if str.isdigit(arr[k][l]):
                        numbers.append(getNumber(arr, k, l))
                numbers = list(dict.fromkeys(numbers))
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]
    return sum


def __main__():
    file = "2023\\Day 3\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))