import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append((line.rstrip('\n')))
    text.close()
    return out

def findIncreases(arr):
    ver = 0
    down = 0
    aim = 0
    for row in arr:
        command = row.split()[0]
        dist = int(row.split()[1])
        if command == "up":
            aim -= dist
        elif command == "down":
            aim += dist
        elif command == "forward":
            ver += dist
            down += aim*dist
    return ver, down

def __main__():
    file = "Day 2\input-1.txt"
    arr = readFile(file)
    ver, down  = findIncreases(arr)
    print(ver * down)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))