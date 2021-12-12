import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(line.rstrip('\n').split("-"))
    text.close()
    return out

def makeTree(arr):
    dic = {}
    for row in arr:
        if row[0] in dic:
            dic[row[0]].append(row[1])
        else:
            dic[row[0]] = [row[1]]
        if row[1] in dic:
            dic[row[1]].append(row[0])
        else:
            dic[row[1]] = [row[0]]
    return dic


def findPaths(tree, start, visitedLowers, paths, trace):
    for connection in tree[start]:
        returnPath = []
        if connection in visitedLowers:
            pass
        elif connection == "end":
            trace.append(connection)
            paths.append(trace.copy())
            trace.pop(-1)
        elif connection.islower():
            trace.append(connection)
            visitedLowers.append(connection)
            findPaths(tree, connection, visitedLowers, paths, trace)
            trace.pop(-1)
            visitedLowers.pop(-1)
        else:
            trace.append(connection)
            findPaths(tree, connection, visitedLowers, paths, trace)
            trace.pop(-1)
    return paths


def __main__():
    file = "Day 12\input.txt"
    arr = readFile(file)
    tree = makeTree(arr)
    visitedLowers = ["start"]
    paths = []
    trace = []
    paths = findPaths(tree, "start", visitedLowers, paths, trace)
    print(len(paths))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))