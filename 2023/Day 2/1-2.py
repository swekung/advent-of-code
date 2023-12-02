import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for line in text:
        out.append((line.rstrip('\n')))
    return out

def solve(arr):
    sum = 0

    for (i, line) in enumerate(arr):
        line = line.split(":")[1]
        valid = True
        red = 0
        blue = 0
        green = 0
        for group in line.split(";"):
            
            for pair in group.split(","):
                col = pair.split(" ")[2]
                num = int(pair.split(" ")[1])
                if col == "red" and num > red:
                    red = num
                elif col == "blue" and num > blue:
                    blue = num
                elif col == "green" and num > green:
                    green = num                
        sum += red * blue * green
    return sum


def __main__():
    file = "2023\\Day 2\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))