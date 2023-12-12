import numpy as np
import sys
import time
import re
from operator import itemgetter
from functools import cache
start_time = time.time()


def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        groups = [re.findall("[?#.]+", row)[0] for i in range(5)]
        springs = [int(i) for i in re.findall("\\d+", row)]
        out.append(["?".join(groups) + ".", springs*5])
    return out

@cache
def getcount(line, counts, pos, current_count, countpos):
      # pos is the next character to be processed
      # current_count is how far into the current sequence of #s we are in
      # countpos is how many sequences of #s we have already finished
      if pos == len(line):
            ret = 1 if len(counts) == countpos else 0
      elif line[pos] == '#':
            ret = getcount(line, counts, pos + 1, current_count + 1, countpos)
      elif line[pos] == '.' or countpos == len(counts):
            if countpos < len(counts) and current_count == counts[countpos]:
                  ret = getcount(line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  ret = getcount(line, counts, pos + 1, 0, countpos)
            else:
                  ret = 0
      else:
            hash_count = getcount(line, counts, pos + 1, current_count + 1, countpos)
            dot_count = 0
            if current_count == counts[countpos]:
                  dot_count = getcount(line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  dot_count = getcount(line, counts, pos + 1, 0, countpos)
            ret = hash_count + dot_count
      return ret

def solve(arr):
    arrangements = 0
    for row in arr:
        arrangements += getcount(row[0], tuple(row[1]), 0, 0, 0)
    return arrangements

def __main__():
    file = "2023\\Day 12\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))