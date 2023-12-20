from functools import cache
import numpy as np
import sys
import time
import re
from operator import itemgetter
import heapq
from collections import defaultdict, Counter, deque
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
dist = 0

def newRange(op, n, lo, hi):
  if op=='>':
    lo = max(lo, n+1)
  elif op=='<':
    hi = min(hi, n-1)
  elif op=='>=':
    lo = max(lo, n)
  elif op=='<=':
    hi = min(hi, n)
  else:
    assert False
  return (lo,hi)

def newRanges(var, op, val, xl, xh, ml, mh, al, ah,sl, sh):
    if var=='x':
        xl,xh = newRange(op, val, xl, xh)
    elif var=='m':
        ml,mh = newRange(op, val, ml, mh)
    elif var=='a':
        al,ah = newRange(op, val, al, ah)
    elif var=='s':
        sl,sh = newRange(op, val, sl, sh)
    return (xl,xh,ml,mh,al,ah,sl,sh)

def process(steps):
    ans = 0
    Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1,4000)])
    while Q:
        state, xl,xh,ml,mh,al,ah,sl,sh = Q.pop()
        if xl>xh or ml>mh or al>ah or sl>sh:
            continue
        if state == "A":
            score = (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
            ans += score
            continue
        elif state == "R":
            continue
        else:
            step = steps[state]
            for cmd in step:
                res = cmd
                if ":" in cmd:
                    cond, res = cmd.split(":")
                    var = cond[0]
                    op = cond[1]
                    val = int(re.findall("\\d+", cond)[0])
                    Q.append((res, *newRanges(var, op, val, xl, xh, ml, mh, al, ah,sl, sh)))
                    xl,xh,ml,mh,al,ah,sl,sh = newRanges(var, '<=' if op=='>' else '>=', val, xl, xh, ml, mh, al, ah,sl, sh)
                else:
                    Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))
    return ans


def solve(steps, parts):
    print(process(steps))
    return 

def __main__():
    file = "2023\\Day 19\\input.txt"
    steps, parts = readFile(file)
    print(solve(steps, parts))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))