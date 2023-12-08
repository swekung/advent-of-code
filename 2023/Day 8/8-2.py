import math
import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = {}
    instructions = text[0].rstrip("\n")
    starters = []
    finishers = []
    for row in text[2:]:
        tmp = re.findall("\\w{3}", row)
        out[tmp[0]] = (tmp[1], tmp[2])
        if tmp[0][2] == "A":
            starters.append(tmp[0])
        if tmp[0][2] == "Z":
            finishers.append(tmp[0])
    return out, instructions, starters, finishers

def solve(map, instructions, starters, finishers):
    steps = 0
    for (i, pos) in enumerate(starters):
        steps = 0
        while not pos.endswith("Z"):
            instruction = instructions[steps % len(instructions)]
            if instruction == "R":
                pos = map[pos][1]
            else:
                pos = map[pos][0]
            steps += 1
        starters[i] = steps
    return math.lcm(*starters)
    




def __main__():
    file = "2023\\Day 8\\input.txt"
    map, instructions, starters, finishers = readFile(file)
    print(solve(map, instructions, starters, finishers))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))