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
    if len(maps) == 0:
        return seeds
    min = float('inf')
    locations = []
    for seed in seeds:
        found = 0
        for loc in maps[0][1:]:
            if not found:
                if seed >= int(loc[1]) and seed <= (int(loc[1]) + int(loc[2])):
                    found = True
                    diff = seed - int(loc[1])
                    location = int(loc[0]) + diff
        if not found:
            location = seed
        locations.append(location)
    return solve(locations, maps[1:])    


def __main__():
    file = "2023\\Day 5\\input.txt"
    maps, seeds = readFile(file)
    print(min(solve(seeds, maps)))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))