import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(list(line.rstrip('\n')))
    text.close()
    return out

def solve(arr):
    sum = 0
    opening = ['[', "(", "{", "<"]
    closing = ["]", ")", "}", ">"]
    matching = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = {"]": 57, ")": 3, "}": 1197, ">": 25137}
    for row in arr:
        openStack = []
        for char in row:
            if char in opening:
                openStack.insert(0, char)
            else:
                if not matching[char] == openStack.pop(0):
                    sum += scores[char]
                    break
    return sum

def __main__():
    file = "Day 10\input.txt"
    arr = readFile(file)
    sum = solve(arr)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))