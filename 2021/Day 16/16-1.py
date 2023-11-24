from typing import Counter
import numpy as np
import sys
import time
import networkx as nx
start_time = time.time()

hexDict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
    }
def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out = list(line.rstrip('\n'))
    text.close()
    newOut = []
    for char in out:
        newOut += hexDict[char]
    return newOut

def binStrToInt(binary_str):
    length = len(binary_str)

    num = 0
    for i in range(length):
        num = num + int(binary_str[i])
        num = num * 2
    return int(num / 2)

def parse(arr, totVer):
    ver = binStrToInt(arr[:3])
    totVer += ver
    arr = arr[3:]
    typeID = binStrToInt(arr[:3])
    arr = arr[3:]
    if typeID == 4:
        binStr = []
        while arr[0] == '1':
            binStr += arr[1:5]
            arr = arr[5:]
        binStr += arr[1:5]
        arr = arr[5:]
        val = binStrToInt(binStr)
    else:
        lenType = binStrToInt(arr[:1])
        arr = arr[1:]
        if lenType == 0:
            packLen = binStrToInt(arr[:15])
            arr = arr[15:]
            tempDic = arr[:packLen]
            while not len(tempDic) == 0:
                tempDic, totVer = parse(tempDic, totVer)
            arr = arr[packLen:]
        else:
            packLen = binStrToInt(arr[:11])
            arr = arr[11:]
            for i in range(packLen):
                arr, totVer = parse(arr, totVer)
    return arr, totVer



def __main__():
    file = "Day 16/input.txt"
    arr = readFile(file)
    totV = parse(arr, 0)
    print(totV)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))