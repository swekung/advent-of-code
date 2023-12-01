import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.read()
    
    text = text.replace("one", "one1one")
    text = text.replace("two", "two2two")
    text = text.replace("three", "three3three")
    text = text.replace("four", "four4four")
    text = text.replace("five", "five5five")
    text = text.replace("six", "six6six")
    text = text.replace("seven", "seven7seven")
    text = text.replace("eight", "eight8eight")
    text = text.replace("nine", "nine9nine")


    out = []

    for line in text.split():
        first = None
        last = None
        for c in line:
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