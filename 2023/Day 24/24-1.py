from functools import cache
import numpy as np
import sys
import time
from z3 import Int, Solver, sat
from itertools import combinations
import networkx as nx
import re
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        out.append([int(x) for x in re.findall("(-*\d+)", row.strip("\n"))])
    return out

def solve(hailstones, lower, upper):
    ret = 0
    for (x1, y1, _, vx1, vy1, _), (x2, y2, _, vx2, vy2, _) in combinations(hailstones, 2):
        solver = Solver()
        t = Int("t")
        solver.add(t > 0)
        solver.add(x1 + vx1 * t == x2 + vx2 * t)
        solver.add(y1 + vy1 * t == y2 + vy2 * t)
        if solver.check() == sat:
            m = solver.model()
            if m.eval(t).as_long() >= 0:
                ret += 1
    return ret

def __main__():
    file = "2023\\Day 24\\input.txt"
    flips = readFile(file)
    print(solve(flips, 200000000000000, 400000000000000))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))