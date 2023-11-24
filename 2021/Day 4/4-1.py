import sys
import time
import numpy as np
import re
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    outTemp = []
    numDraw = []
    temp = []
    for line in text:
        for i in re.split(" |,", line.strip('\n')):
            if i.isnumeric():
                temp.append(int(i))
        if(line == '\n'):
            if(not len(outTemp) <= 1):
                out.append(outTemp)
            outTemp = []
            temp = []
        elif(line[2] == ',' or line[3] == ','):
            numDraw = temp
            temp = []
            outTemp = []
        if(not len(temp) <= 1):
            outTemp.append(temp)
        temp = []
    out.append(outTemp)
    text.close()
    return out, numDraw

def checkBingo(board, empties):
    for i in range(len(board)):
        sum = 0
        for j in range(len(board[i])):
           sum += empties[i][j]
        if sum >= len(board):
            return True
    for i in range(len(board)):
        sum = 0
        for j in range(len(board[i])):
           sum += empties[j][i]
        if sum >= len(board):
            return True
    return False

def playBingo(boards, draws):
    emptyBoards = np.zeros(np.array(boards).shape)
    for draw in draws:
        for i in range(len(boards[0])):
            for j in range(len(boards[0][i])):
                for k in range(len(boards)):
                    if boards[k][i][j] == draw:
                        emptyBoards[k][i][j] = 1
        for i in range(len(boards)):
            if checkBingo(boards[i], emptyBoards[i]):
                return boards[i], emptyBoards[i], draw

        
def calcScore(board, mask, draw):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if mask[i][j] == 0:
                score += board[i][j]
    return score * draw

def main():
    file = "Day 4\input.txt"
    cards, numDraw = readFile(file)
    winBoard, winMask, finalDraw = playBingo(cards, numDraw)
    print(calcScore(winBoard,winMask,finalDraw))

main()
print("--- %s seconds ---" % (time.time() - start_time))