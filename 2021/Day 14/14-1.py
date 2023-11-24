from typing import Counter
import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(line.rstrip('\n'))
    text.close()
    return out

def solve(rules, start, itterations):
    newString = list(start).copy()
    start = list(start).copy()
    for i in range(itterations):
        insert = {}
        for rule in rules:
            rulePair = rule.split()[0]
            ruleInsert = rule.split()[2]
            for j in range(len(start) - 1):
                if start[j] + start[j+1] == rulePair:
                    insert[j] = ruleInsert
        for i in range(len(start), -1, -1):
            if i in insert:
                newString.insert(i + 1, insert[i])
        start = newString.copy()
    return start

def calcScore(string):
    count = Counter(string)
    mostCommon = count.most_common(1)
    leastCommon = count.most_common()[-1]
    return mostCommon[0][1] - leastCommon[1]

def __main__():
    file = "Day 14\input.txt"
    arr = readFile(file)
    start = arr.pop(0)
    arr.pop(0)
    string  = solve(arr, start, 10)
    sum = calcScore(string)
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))