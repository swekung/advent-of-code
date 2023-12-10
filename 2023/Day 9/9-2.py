import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        tmp = re.findall("(-*\\d+)", row)
        out.append([int(i) for i in row.strip("\n").split()])
    return out


def calcSteps(arr):
    return [arr[i+1] - arr[i] for i in range(len(arr)-1)]

def extrapolate(xs):
  tmp = calcSteps(xs)
  if sum(xs) == 0:
    return 0
  else:
    return xs[-1] + extrapolate(tmp)

def solve(arr):
    tot = 0
    for seq in arr:
        tot += extrapolate(seq[::-1])
    return tot

def __main__():
    file = "2023\\Day 9\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))