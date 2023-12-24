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
        out.append([int(x) for x in re.findall("(-*\\d+)", row.strip("\n"))])
    return out

def solve(hailstones):
    solver = Solver()
    x, y, z, vx, vy, vz = map(Int, ('x', 'y', 'z', 'vx', 'vy', 'vz'))
    for i, (a, b, c, va, vb, vc) in enumerate(hailstones[:3]):
        t = Int(f"t{i}")
        solver.add(t > 0)
        solver.add(x + vx * t == a + va * t)
        solver.add(y + vy * t == b + vb * t)
        solver.add(z + vz * t == c + vc * t)
    if solver.check() == sat:
        m = solver.model()
        return sum(m.eval(var).as_long() for var in (x, y, z))

def __main__():
    file = "2023\\Day 24\\input.txt"
    flips = readFile(file)
    print(solve(flips))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))