import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.read()
    out = []
    for row in text.split(","):
        lens = re.findall("\\w+", row)[0]
        op = re.findall("[=-]", row)[0]
        if op == "=":
            foc = int(re.findall("\\d+", row)[0])
        else:
            foc = None
        out.append(([*lens], op, foc))
    return out
        
def getTarget(arr, i, j):
    rocks = 0
    for i in range(i, -1, -1):
        if arr[i][j] == "O":
            rocks += 1
        if arr[i][j] == "#":
            return len(arr) - i - rocks
    return len(arr) - i - rocks + 1

def hash(label):
    sum = 0
    for char in label:
        sum += ord(char)
        sum *= 17
        sum = sum % 256
    return sum

def checkIn(label, box):
    i = 0
    for (i, set) in enumerate(box):
        if set[0] == label:
            return True, i
    return False, i

def solve(arr, boxes):
    sum = 0
    for set in arr:
        lens = set[0]
        op = set[1]
        foc = set[2]
        s = hash(lens)
        check, i = checkIn(lens, boxes[s]) 
        if op == "=":
            if check:
                boxes[s][i] = set
            else:
                boxes[s].append(set)
        elif op =="-":
            if check:
                boxes[s].pop(i)   
    return boxes

def score(boxes):
    sum = 0
    for (j, box) in enumerate(boxes):
        for (i, lens) in enumerate(box):
            sum += (j+1) * (i+1) * lens[2]
    return sum

def __main__():
    file = "2023\\Day 15\\input.txt"
    boxes = [[] for i in range(256)]
    arr = readFile(file)
    boxes = solve(arr, boxes)
    print(score(boxes))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))