import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()

labelsNoJ = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
labels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

wins = []

def readFile(file):
    with open(file) as f:
        text = f.readlines()
    out = []
    for row in text:
        hand = [*row.split(" ")[0]]
        bid = int(row.split(" ")[1].rstrip("\n"))
        out.append((hand, bid))
    return out

def getType(hand):
    
    occurences = []

    j = hand[0].count("J")

    rank = 0
    for label in labelsNoJ:
        occurences.append(hand[0].count(label))
    if 5-j in occurences:
        rank = 6
    elif 4-j in occurences:
        rank = 5
    elif 3 in occurences and 2 in occurences:
        rank = 4
    elif 3-j in occurences and occurences.count(2) == 2:
        rank = 4
    elif 2 in occurences and 1 in occurences and j == 2:
        rank = 4
    elif 3 in occurences and 2-j in occurences:
        rank = 4
    elif 3-j in occurences:
        rank = 3
    elif occurences.count(2) == 2:
        rank = 2
    elif 2 in occurences and 1 in occurences and j == 1:
        rank = 2
    elif 2-j in occurences:
        rank = 1
    else:
        rank = 0
    
    return (hand[0], hand[1], rank)

def replaceLabel(hand):
    cards = hand[0]
    for (i, label) in enumerate(labels):
        cards = [x if x != label else i for x in cards]
    return (cards, hand[1], hand[2])

def calcWinnings(ranked):
    sum = 0
    for (i, hand) in enumerate(ranked):
        sum += (i+1) * hand[1]
    return sum


def solve(hands):
    ranked = []
    for hand in hands:
        ranked.append(getType(hand))

    labels.reverse()
    for i in range(len(ranked)):    
        ranked[i] = replaceLabel(ranked[i])
            
    ranked = sorted(ranked)
    ranked = sorted(ranked,key=itemgetter(2))
    
    return calcWinnings(ranked)
    




def __main__():
    file = "2023\\Day 7\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))