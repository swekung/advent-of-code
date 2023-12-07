import numpy as np
import sys
import time
import re
from operator import itemgetter
start_time = time.time()

labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

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

    for label in labels:
        occurences.append(hand[0].count(label))
    if 5 in occurences:
        return (hand[0], hand[1], 6)
    if 4 in occurences:
        return (hand[0], hand[1], 5)
    if 3 in occurences and 2 in occurences:
        return (hand[0], hand[1], 4)
    if 3 in occurences:
        return (hand[0],hand[1],  3)
    if occurences.count(2) is 2:
        return (hand[0], hand[1], 2)
    if 2 in occurences:
        return (hand[0], hand[1], 1)
    return (hand[0], hand[1], 0)

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
            

    ranked = sorted(ranked,key=itemgetter(2))
    
    j = 0
    tmpRanked = []
    for i in range(7):
        slice = []
        for hand in ranked:
            if hand[2] == i:
                slice.append(hand)
        tmpRanked += sorted(slice)


    return calcWinnings(tmpRanked)
    




def __main__():
    file = "2023\\Day 7\\input.txt"
    arr = readFile(file)
    print(solve(arr))


__main__()
print("--- %s seconds ---" % (time.time() - start_time))