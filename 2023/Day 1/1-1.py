import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for line in text:
        first = None
        last = None
        for c in line.rstrip('\n'):
            
            if c.isdigit():
                if first == None:
                    first = c
                else:
                    last = c
        if last == None:
            out.append(int(first+first))
        else:
            out.append(int(first+last))
    return out

        

def __main__():
    file = "2023\\Day 1\\input.txt"
    arr = readFile(file)
    print(sum(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))