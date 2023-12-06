import numpy as np
import sys
import time
import re
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    out = zip(re.findall(r'\d+', text[0].strip(" ")), re.findall(r'\d+', text[1].strip(" "))) 
    t, d= "", ""
    for (time, dist) in out:
        t += time
        d += dist
    return t, d

def solve(time, dist):
    time = int(time)
    dist = int(dist)
    start, stop = 0, time
    speed = 0
    while speed * (time - start) <= dist:
        start += 1
        speed += 1
    speed = time
    while speed * (time - stop) <= dist:
        stop -= 1
        speed -= 1
    winners = time - (start-1) - (time - stop)
    return winners




def __main__():
    file = "2023\\Day 6\\input.txt"
    t, d = readFile(file)
    print(solve(t, d))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))