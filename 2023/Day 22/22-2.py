from functools import cache
import numpy as np
import sys
import time
import re
from collections import defaultdict, Counter, deque
import heapq
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    bricks = {}
    id = 0
    for row in text:
        ends = row.split("~")
        brick = []
        for end in ends:
            tmp = [int(r) for r in re.findall("\d+", end)]
            brick.append(tmp)
        bricks[id] = brick
        id += 1
    return bricks

def findNext(bricks):
    for id in bricks:
        above = []
        bellow = []
        start = bricks[id][0]
        end = bricks[id][1]
        adj = [[(i,j) for j in range(start[1], end[1]+1)] for i in range(start[0], end[0]+1)]
        for row in adj:
            for (i, j) in row:
                up = float('inf')
                down = 0
                for idS in bricks:
                    if id == idS:
                        pass
                    else:
                        startS = bricks[idS][0]
                        endS = bricks[idS][1]
                        if startS[0] <= i and i <= endS[0] and startS[1] <= j and j <= endS[1]:
                            if start[2] < startS[2] and startS[2] < up:
                                up = startS[2]
                                if not idS in above:
                                    above.append(idS)
                            elif startS[2] < start[2] and down < startS[2]:
                                down = startS[2]
                                if not idS in bellow:
                                    bellow.append(idS)
        bricks[id].append(bellow)
        bricks[id].append(above)
        bricks[id].append([])
    return bricks

def fall(bricks):
    new = []
    sortedBricks = [(bricks[id][0][2], id) for id in bricks]
    sortedBricks.sort()
    for (z, id) in sortedBricks:
        height = bricks[id][1][2] - bricks[id][0][2]
        z = 1
        for idS in bricks[id][2]:
            zS = bricks[idS][1][2]
            if zS + 1 > z:
                z = zS + 1
        bricks[id][0][2] = z
        bricks[id][1][2] = z + height
    return bricks
            
def canDis(id, bricks):
    z = bricks[id][1][2]
    for brick in bricks[id][3]:
        if bricks[brick][0][2] == z + 1:
            adjDown = 0
            for downAdj in bricks[brick][2]:
                if bricks[downAdj][1][2] + 1 == bricks[brick][0][2]:
                    adjDown += 1
            if adjDown <= 1:
                return False
    return True

def connected(id1, id2, bricks):
    z1 = bricks[id1][1][2]
    z2 = bricks[id2][0][2]
    return z1 == z2-1


def solve(bricks):
    sum = 0
    bricks = findNext(bricks)
    bricks = fall(bricks)
    for id in bricks:
        if not canDis(id, bricks):
            lastFallen = [id]
            new = bricks[id][3]
            fallen = []
            lastItter = [None]
            while lastItter != fallen:
                lastItter = fallen
                fallen = []
                for id in new:
                    sup = bricks[id][2]
                    add = True
                    for su in sup:
                        if (not su in lastFallen or id in fallen) and connected(su, id, bricks):
                            add = False
                    if add:
                        fallen.append(id)
                new = []
                for id in fallen:
                    for id1 in bricks[id][3]:
                        if not id1 in new and connected(id, id1, bricks):
                            new.append(id1)
                lastFallen += fallen
            sum += len(lastFallen) - 1
    return sum

def __main__():
    file = "2023\\Day 22\\input.txt"
    bricks = readFile(file)
    print(solve(bricks))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))