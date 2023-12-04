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

def findMatches(arr1, arr2):
    out = []
    for i in arr1:
        for j in arr2:
            if str.isnumeric(i) and str.isnumeric(j) and i == j:
                out.append(i)
    return out

def updateAmount(arr, n, num):
    for i in range(n+1, n+num+1):
        arr[i] += 1 * arr[n]
    return arr

def solve(arr):
    sum = 0
    new = []
    winners = [1] * len(arr)
    for (i, row) in enumerate(arr):
        row = row.split(":")[1]
        win = row.split("|")[0].split(" ")
        hand = row.split("|")[1].split(" ")
        matches = findMatches(win, hand)
        if len(matches) == 0:
            pass
            #new.append(0)
        else:
            winners = updateAmount(winners, i, len(matches))
            sum += 2**(len(matches)-1) * winners[i]
    return winners

def __main__():
    file = "2023\\Day 4\\input.txt"
    arr = readFile(file)
    ret = solve(arr)
    print(sum(ret))

def getArrLen(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

__main__()
print("--- %s seconds ---" % (time.time() - start_time))