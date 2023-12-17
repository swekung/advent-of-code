from functools import cache
import numpy as np
import sys
import time
import re
from operator import itemgetter
import heapq
start_time = time.time()


class State:
	def __init__(self, loss, p, d, c):
		self.loss = loss
		self.p = p
		self.d = d
		self.c = c
		self.key = (self.p, self.d, self.c)
	def __lt__(self, other):
		return (self.loss, self.c)<(other.loss, other.c)

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        out.append(re.findall("\\d", row.rstrip("\n")))
    return out
        
# return all elements adjacent to arr[i][j], above bello left right
def getAdjacents(arr, i, j, prev):
    adj = []
    last = [-10, -10]
    up, down, left, right = 0,0,0,0
    for v in prev:
        if None in prev:
            break
        if v[0] == last[0] and v[1] == last[1]+1:
            right += 1
        else:
            right = 0
        if v[0] == last[0] and v[1] == last[1]-1:
            left += 1
        else:
            left = 0
        if v[0] == last[0]+1 and v[1] == last[1]:
            down += 1
        else:
            down = 0
        if v[0] == last[0]-1 and v[1] == last[1]:
            up += 1
        else:
            up = 0
        last = v
    if i > 0 and up < 3:
        adj.append(arr[i-1][j])
    if i < len(arr) - 1 and down < 3:
        adj.append(arr[i+1][j])
    if j > 0 and left < 3:
        adj.append(arr[i][j-1])
    if j < len(arr[i]) - 1 and right < 3:
        adj.append(arr[i][j+1])
    return adj

def getMinDist(arr):
    min = float('inf')
    for (i, v) in enumerate(arr):
        if v[2] < min:
            min = i
    return min

def solve(arr):
    grid = {}
    P = complex
    for (i, row) in enumerate(arr):
        for (j, elem) in enumerate(row):
            grid[P(i,j)] = int(elem)
    
    seen = set()
    q = [State(0,0,1,0), State(0,0,1j,0)]

    while q:
        s = heapq.heappop(q)

        if s.key in seen:
            continue
        seen.add(s.key)
        loss, p, d, c = s.loss, s.p, s.d, s.c

        if p == P(len(arr[0])-1, len(arr)-1) and c >= 4:
            return loss
        
        if c < 10 and p+d in grid:
            heapq.heappush(q, State(loss+grid[p+d], p+d, d, c+1))
        
        d *= 1j
        if p+d in grid and 4<=c:
            heapq.heappush(q, State(loss+grid[p+d], p+d, d, 1))
        
        d *= -1
        if p+d in grid and 4<=c:
            heapq.heappush(q, State(loss+grid[p+d], p+d, d, 1))
    return s
        

def __main__():
    file = "2023\\Day 17\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))