from collections import Counter, defaultdict, deque

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(15, 2024)


def parse_raw(raw: str):
    dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    data = raw.split("\n\n")
    moves = [dirs[d] for d in data[1] if d in dirs]

    map = []

    for row in data[0].splitlines():
        map.append(list(row))


    return map, moves


data = parse_raw(raw)

def print_map(map):
    for row in map:
        print("".join(row))

def score_map(map):
    score = 0
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == "O" or c == "[":
                score += 100 * i + j
    return score

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    map, moves = data
    print_map(map)
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == "@":
                pi, pj = i, j
                map[i][j] = "."
    
    for di, dj in moves:
        map[pi][pj] = "."
        if map[pi + di][pj + dj] == ".":
            pi += di
            pj += dj
        elif map[pi + di][pj + dj] == "#":
            pass
        else:
            ti, tj = pi, pj
            while map[ti + di][tj + dj] == "O":
                ti += di
                tj += dj
            if map[ti + di][tj + dj] == ".":
                map[ti + di][tj + dj] = "O"
                map[pi + di][pj + dj] = "."
                pi += di
                pj += dj
        map[pi][pj] = "@"
    return score_map(map)
        



aoc_helper.lazy_test(day=15, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    map, moves = data
    t = {"#": "##", "O": "[]", "@": "@."}
    new_map = [["." for _ in range(len(map[0]) * 2)] for _ in range(len(map))]
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c in t:
                c = t[c]
                for k, d in enumerate(c):
                    new_map[i][2 * j + k] = d
    map = new_map


    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == "@":
                pi, pj = i, j


    for di, dj in moves:
        map[pi][pj] = "."
        if map[pi + di][pj + dj] == ".":
            pi += di
            pj += dj
        elif map[pi + di][pj + dj] == "#":
            pass
        else:
            ti, tj = pi, pj
            if di == 0:
                while map[ti + di][tj + dj] in ["[", "]"]:
                    ti += di
                    tj += dj
                if map[ti + di][tj + dj] == ".":
                    l = 0
                    for k in range( 2 * dj + pj, tj + (2*dj), dj):
                        mod_op = 0 if dj == 1 else 1
                        map[ti + di][k] = "[" if l % 2 == mod_op else "]"
                        l += 1
                    map[pi + di][pj + dj] = "."
                    pi += di
                    pj += dj
            else:
                if map[ti + di][tj + dj] == "[":
                    j_to_push = [set([pj, pj + 1])]
                else:
                    j_to_push = [set([pj - 1, pj])]
                blocked = False
                while True:
                    ti += di
                    if len(j_to_push[-1]) == 0:
                        j_to_push.pop()
                        while len(j_to_push) != 0:
                            es = j_to_push.pop()
                            for e in es:
                                map[ti][e] = map[ti - di][e]
                                map[ti - di][e] = "."
                            ti -= di
                        pi += di
                        break

                    t_push = set()
                    for j in j_to_push[-1]:
                        if map[ti + di][j] == "[":
                            t_push.add(j + 1)
                            t_push.add(j)
                        if map[ti + di][j] == "]":
                            t_push.add(j - 1)
                            t_push.add(j)
                        if map[ti + di][j] == "#":
                            blocked = True
                    j_to_push.append(t_push)

                    for j in j_to_push[-1]:
                        if map[ti + di][j] == "#":
                            blocked = True
                    if blocked:
                        break
                

                
        map[pi][pj] = "@"
    #print_map(map)
    return score_map(map)


aoc_helper.lazy_test(day=15, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=15, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=15, year=2024, solution=part_two, data=data)
