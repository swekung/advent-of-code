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

def parse(arr):
    dic = {}
    folds = []
    height = 0
    width = 0
    for row in arr:
        if "fold" in row:
            out = row.split()[-1].split("=")
            folds.append(out)
        elif len(row) == 0:
            pass
        else:
            dic[row] = 1
            x, y = row.split(",")
            if int(x) > width:
                width = int(x)
            if int(y) > height:
                height = int(y)
    return dic, folds, height, width


def fold(dic, fold, steps, height, width):
    #printdic(dic, height, width)
    for i in range(steps):
        if "x" in fold[i][0]:
            for j in range(int(fold[i][1])+1, width+1):
                for k in range(height+1):
                    if str(j) + "," + str(k) in dic:
                        dic[str(2* int(fold[i][1]) - j) + "," +  str(k)] = 1
                        dic.pop(str(j) + "," + str(k))
            width = int(int(fold[i][1]) - 1)
        if "y" in fold[i][0]:
            for j in range(int(fold[i][1])+1, height+1):
                for k in range(width+1):
                    if str(k) + "," + str(j) in dic:
                        newCoord = str(2*int(fold[i][1]) - j)
                        dic[str(k) + "," +  str(2 * int(fold[i][1]) - j)] = 1
                        dic.pop(str(k) + "," + str(j))
            height = int(fold[i][1]) - 1
        #printdic(dic, height, width)
    return dic

def printdic(dic, height, width):
    for i in range(height+1):
        lineBuf = []
        for j in range(width+1):
            if str(j) + "," + str(i) in dic:
                lineBuf += "#"
            else:
                lineBuf += "."
        print(lineBuf)
    return

def __main__():
    file = "Day 13\input.txt"
    arr = readFile(file)
    dic, folds, height, width = parse(arr)
    fold(dic, folds, 1, height, width)
    print(len(dic))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))