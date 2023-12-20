from functools import cache
import numpy as np
import sys
import time
import re
from collections import defaultdict, Counter, deque
import heapq
start_time = time.time()

class Module:
    def __init__(self, name, type, goals, state) -> None:
        self.name = name
        self.type = type
        self.goals = goals
        self.state = state
        self.recv = {}

    def getName(self):
        return self.name
    
    def getGoals(self):
        return self.goals

    def addSender(self, sender):
        self.recv[sender] = False

    def press(self, state, sender):
        self.recv[sender] = state
        goals = self.goals
        if self.type == "broadcaster":
            self.state = state
        elif self.type == "button":
            self.state = False
        elif self.type == "output":
            self.state = state
        elif self.type == "%":
            if not state:
                self.state = not self.state
            else:
                goals = []
        elif self.type == "&":
            self.state = False
            for key in self.recv:
                if not self.recv[key]:
                    self.state = True
        return self.state, goals, self.name
        
                


def readFile(file):
    with open(file) as f:
        text = f.readlines()
    modules = {}
    for row in text:
        name = re.findall("\\w+", row)[0]
        type = re.findall("[%&]|(broadcaster)|(button)", row)[0]
        if type != "boradcaster" or type != "button":
            type = row[0]
        goals = re.findall("\\w+", row.split(">")[1])
        modules[name] = Module(name, type, goals, False)
    modules["output"] = Module("output", "output", [], False)
    for mod in modules:
        mod = modules[mod]
        for g in mod.getGoals():
            if g in modules:
                modules[g].addSender(mod.getName())
    return modules

def solve(modules):
    sumL, sumH = 0, 0
    seen = []
    Q = []
    [Q.append((False, ["button"], "")) for i in range(1)]
    sender = ""
    for i in range(1000):
        Q = []  
        Q.append((False, ["broadcaster"], "button"))
        while Q:
            state, goals, sender = Q.pop(0)
            if state:
                sumH += 1 * len(goals)
            else:
                sumL += 1 * len(goals)
            for goal in goals:
                #print(f"{sender} -{"high" if state else "low"}-> {goal}")
                if goal in modules:
                    s, gs, n = modules[goal].press(state, sender)
                    if not n == "output":
                        Q.append((s, gs, n))
    return sumL * sumH

def __main__():
    file = "2023\\Day 20\\input.txt"
    modulues = readFile(file)
    print(solve(modulues))



__main__()
print("--- %s seconds ---" % (time.time() - start_time))