import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append((line.rstrip('\n').split("|")))
    text.close()
    return out

def findKey(arr):
    dic = []
    for row in arr:
        outDict = {}
        i = 0
        rowChars = row[0].split() + row[1].split()
        rightSide = ""
        four = ""
        89 = ""
        while not containsAll(outDict):
            length = len(rowChars[i])
            if length == 2:
                outDict[rowChars[i]] =  1
                rightSide = rowChars[i]
            elif length == 3:
                outDict[rowChars[i]] =  7
            elif length == 7:
                outDict[rowChars[i]] =  8
            elif length == 4:
                outDict[rowChars[i]] =  4
                four = rowChars[i]
            elif length == 6:
                if not (len(rightSide) == 2 and len(four) == 4):
                    pass
                elif not checkIfChars(rightSide, rowChars[i]):
                    outDict[rowChars[i]] = 6
                elif not checkIfChars(four, rowChars[i]):
                    outDict[rowChars[i]] = 0
                elif 9 not in outDict.values():
                    outDict[rowChars[i]] = 9
                    89 = rowChars[i]
            elif length == 5:
                if not (len(rightSide) == 2 and len(89) == 6):
                    pass
                elif checkIfChars(rightSide, rowChars[i]):
                    outDict[rowChars[i]] = 3
                elif checkIfChars(rowChars[i], 89):
                    outDict[rowChars[i]] = 5
                elif 2 not in outDict.values():
                    outDict[rowChars[i]] = 2
            if i == len(rowChars) - 1:
                i = 0
            else:
                i += 1
        dic.append(outDict)
    return dic

def containsAll(dic):
    arr = np.zeros(10)
    for key in dic.keys():
        if arr[dic[key]] == 0:
            arr[dic[key]] = 1
    return np.sum(arr) == 10


def checkIfChars(smallStr, largeStr):
    for char in smallStr:
        if not char in largeStr:
            return False
    return True

def solve(arr, dic):
    out = []
    #dic = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7, "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1, "cdfeb": 5,"fcadb": 3,"cdfeb": 5,"cdbaf": 3,}
    for row in zip(arr, dic):
        rowTot = []
        for string in row[0][1].split():
            length = len(string)
            for key in row[1].keys():
                if checkIfChars(string, key) and checkIfChars(key, string):
                    break
            rowTot.append(row[1][key])
        out.append(int("".join([str(intg) for intg in rowTot])))
    return out

def __main__():
    file = "Day 8\input.txt"
    arr = readFile(file)
    dic = findKey(arr)
    arr = solve(arr, dic)
    sum = 0
    for iintg in arr:
        sum += iintg
    print(sum)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))