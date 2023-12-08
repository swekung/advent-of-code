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
    for row in text[2:]:
        tmp = re.findall("\\w{3}", row)
        out[tmp[0]] = (tmp[1], tmp[2])
    return out, instructions



def solve(map, instructions):
    steps = 0
    pos = "AAA"
    while not pos == 'ZZZ':
        instruction = instructions[steps % len(instructions)]
        if instruction == "R":
            pos = map[pos][1]
        else:
            pos = map[pos][0]
        steps += 1
    return steps
    




def __main__():
    file = "2023\\Day 8\\input.txt"
    map, instructions = readFile(file)
    print(solve(map, instructions))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))