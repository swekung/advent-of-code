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
    mostCommon = []
    leastCommon = []
    for i in range(len(arr[0])):
        zer = 0
        ones = 0
        for row in arr:
            if row[i] is '1':
                ones += 1
            else:
                zer += 1
        if ones > zer:
            mostCommon.append('1')
            leastCommon.append('0')
        else:
            mostCommon.append('0')
            leastCommon.append('1')
    return mostCommon, leastCommon

def binStrToInt(binary_str):


    """The function binStrToInt() takes in one input, a string of ones and
    zeros (no spaces) called BINARY_STR.  It treats that input as a binary
    number (base 2) and converts it to a decimal integer (base 10). It
    returns an integer result."""

    length = len(binary_str)

    num = 0
    for i in range(length):
        num = num + int(binary_str[i])
        num = num * 2
    return num / 2

def __main__():
    file = "Day 3\input.txt"
    arr = readFile(file)
    sol, sol2  = solve(arr)
    sol = binStrToInt(sol)
    sol2 = binStrToInt(sol2)
    print(sol * sol2)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))