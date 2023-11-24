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
        print(i)
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

def solve2(rules, start, itterations):
    ruleOccurences = {}
    ruleMapping = {}
    chars = {}
    length = 0
    for char in start:
        length += 1
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for i in range(len(rules)):
            ruleOccurences[i] = 0
            rulePair = rules[i].split()[0]
            ruleInsert = rules[i].split()[2]
            for j in range(len(start) - 1):
                if start[j] + start[j+1] == rulePair:
                    ruleOccurences[i] += 1
    for i in range(len(rules)):
        rulePair = rules[i].split()[0]
        ruleInsert = rules[i].split()[2]
        ruleOut = rulePair[0] + ruleInsert[0] + rulePair[1]
        ruleMapping[i] = []
        for j in range(len(rules)):
            rulePair = rules[j].split()[0]
            if rulePair in ruleOut:
                ruleMapping[i].append(j)
    for i in range(itterations):
        ruleOccurencesTemp = {}
        for rule in ruleOccurences.keys():
            for mapped in ruleMapping[rule]:
                if mapped in ruleOccurencesTemp:
                    ruleOccurencesTemp[mapped] += ruleOccurences[rule]
                else:
                    ruleOccurencesTemp[mapped] = ruleOccurences[rule]
            length += ruleOccurences[rule]
            if rules[rule].split()[2] in chars:
                chars[rules[rule].split()[2]] += ruleOccurences[rule]
            else:
                chars[rules[rule].split()[2]] = ruleOccurences[rule]
        ruleOccurences = ruleOccurencesTemp.copy()
    return chars

def calcScore(chars):
    max = 0
    for char in chars:
        if chars[char] > max:
            max = chars[char]
    min = max
    for char in chars:
        if chars[char] < min:
            min = chars[char]
    return max, min

def __main__():
    file = "Day 14/input.txt"
    arr = readFile(file)
    start = arr.pop(0)
    arr.pop(0)
    chars  = solve2(arr, start, 40)
    max, min = calcScore(chars)
    print(max - min)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))