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
    outScores = []
    opening = ['[', "(", "{", "<"]
    closing = ["]", ")", "}", ">"]
    matching2 = {"(": ")", "[": "]", "{": "}", "<": ">"}
    matching = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = {"[": 2, "(": 1, "{": 3, "<": 4}
    for row in arr:
        score = 0
        openStack = []
        corrupt = False
        for char in row:
            if char in opening:
                openStack.insert(0, char)
            else:
                if not matching[char] == openStack.pop(0):
                    corrupt = True
                    break
        if not corrupt:
            for i in range(len(openStack)):
                score *= 5
                score += scores[openStack[i]]
            outScores.append(score)
    return outScores

def __main__():
    file = "Day 10\input.txt"
    arr = readFile(file)
    sum = solve(arr)
    sum.sort()
    print(sum[int(len(sum)/2)])


__main__()
print("--- %s seconds ---" % (time.time() - start_time))