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

def solveO2(arr):
    mostCommon = []
    leastCommon = []
    i = 0
    leng = len(arr[0])
    while i < leng:
        zer = 0
        ones = 0
        for row in arr:
            if row[i] is '1':
                ones += 1
            else:
                zer += 1
        if ones >= zer:
            mostCommon.append('1')
            leastCommon.append('0')
        else:
            mostCommon.append('0')
            leastCommon.append('1')
        j = 0
        while j < len(arr):
            if not arr[j][i] is mostCommon[i]:
                arr.pop(j)
            else:
                j += 1
        i += 1
        if len(arr) == 1:
            break
    return arr

def solveCO2(arr):
    mostCommon = []
    leastCommon = []
    i = 0
    leng = len(arr[0])
    while i < leng:
        zer = 0
        ones = 0
        for row in arr:
            if row[i] is '1':
                ones += 1
            else:
                zer += 1
        if ones >= zer:
            mostCommon.append('1')
            leastCommon.append('0')
        else:
            mostCommon.append('0')
            leastCommon.append('1')
        j = 0
        while j < len(arr):
            if not arr[j][i] is leastCommon[i]:
                arr.pop(j)
            else:
                j += 1
        i += 1
        if len(arr) == 1:
            break
    return arr



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
    sol = solveO2(arr)
    sol = binStrToInt(sol[0])
    arr = readFile(file)
    sol2 = solveCO2(arr)
    sol2 = binStrToInt(sol2[0])
    print(sol * sol2)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))