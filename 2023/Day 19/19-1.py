from functools import cache
import numpy as np
import sys
import time
import re
from operator import itemgetter
import heapq
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.read().split("\n\n")
    steps = {}
    for row in text[0].split("\n"):
        workflow = row.split("{")[0]
        checks = row.split("{")[1].rstrip("}").split(",")
        steps[workflow] = checks

    parts = []
    for row in text[1].split("\n"):
        parts.append([int(i) for i in re.findall("\\d+", row)])
    return steps, parts

CAT = ['x', 'm', 'a', 's']

def process(part, step, steps):
    if step == "A":
        return sum(part)
    elif step == "R":
        return 0
    step = steps[step]
    for check in step:
        if not ":" in check:
            return process(part, check, steps)
        else:
            cha = check[0]
            ltgt = check[1]
            val = int(re.findall("\\d+", check)[0])
            nextStep = check.split(":")[1]
            if ltgt == "<" and part[CAT.index(cha)] < val:
                return process(part, nextStep, steps)
            elif ltgt == ">" and part[CAT.index(cha)] > val:
                return process(part, nextStep, steps)


def solve(steps, parts):
    sum = 0
    for part in parts:
        sum += process(part, "in", steps)
    return sum

def __main__():
    file = "2023\\Day 19\\input.txt"
    steps, parts = readFile(file)
    print(solve(steps, parts))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))