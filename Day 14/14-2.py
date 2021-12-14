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
        ruleOut = rulePair[0] + ruleInsert[0] + rulePair[0]
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
        ruleOccurences = ruleOccurencesTemp.copy()
    return ruleOccurences

def calcScore(ruleOccurences, rules):
    chars = {}
    max = ('a', 0)
    for rule in ruleOccurences.keys():
        for char in rules[rule].split()[0]:
            if char in chars:
                chars[char] += ruleOccurences[rule]
            else:
                chars[char] = ruleOccurences[rule]
            if chars[char] > max[1]:
                max = (char, chars[char])
    return chars, max

def __main__():
    file = "Day 14\est.txt"
    arr = readFile(file)
    start = arr.pop(0)
    arr.pop(0)
    ruleOccurences  = solve2(arr, start, 12)
    chars, max = calcScore(ruleOccurences, arr)
    print(max)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))