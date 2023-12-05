import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    seeds = []
    new_seeds = []
    for seed in text[0].split(":")[1].split(" "):
        if str.isnumeric(seed.rstrip("\n")):
            seeds.append(int(seed.rstrip("\n")))
    texts = []
    temp = []
    text = text[2:]
    for line in text:
        if line == "\n":
            texts.append(temp)
            temp = []
        else:
            temp.append(line.rstrip('\n').split(" "))
    texts.append(temp)
    return texts, seeds


def solve(seeds, maps):
    #print(len(maps))
    if len(maps) == 0:
        return seeds
    locations = []
    i = 0
    while i < len(seeds):
        found = 0
        for loc in maps[0][1:]:
            if not found:
                startSeed = seeds[i]
                endSeed = startSeed + seeds[i+1] - 1
                startMap = int(loc[1])
                endMap = startMap + int(loc[2]) - 1

                startInRange = startSeed >= startMap and startSeed <= endMap
                endInRange = endSeed >= startMap and endSeed <= endMap

                if startInRange and endInRange:
                    found = True
                    diff = seeds[i] - int(loc[1])
                    location = [int(loc[0]) + diff, seeds[i+1]]
                elif startInRange:
                    availRange = int(loc[1]) + int(loc[2]) - seeds[i]
                    found = True
                    diff = seeds[i] - int(loc[1])
                    location = [int(loc[0]) + diff, availRange]
                    seeds.append(seeds[i] + availRange)
                    seeds.append(seeds[i+1] - availRange)
                elif endInRange:
                    availRange = seeds[i+1] - (int(loc[1]) - seeds [i])
                    found = True
                    location = [int(loc[0]), availRange]
                    seeds.append(seeds[i])
                    seeds.append(seeds[i+1] - availRange)
        if not found:
            location = [seeds[i], seeds[i+1]]       
        locations += location
        i += 2
    print(totalRange(locations))
    return solve(locations, maps[1:])    

def totalRange(seeds):
    sum = 0
    for i in range(0, len(seeds), 2):
        sum += seeds[i+1]
    return sum

def findMin(seeds):
    min = float('inf')
    for i in range(0, len(seeds), 2):
        if seeds[i] < min:
            min = seeds[i]
    return min

def __main__():
    file = "2023\\Day 5\\input.txt"
    maps, seeds = readFile(file)
    locations = solve(seeds, maps)
    print(findMin(locations))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))