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

raw = aoc_helper.fetch(12, 2024)


def parse_raw(raw: str):
    return raw.splitlines()


data = parse_raw(raw)

def neigh(map, x, y, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny][0] == c:
            neighbors.append((nx, ny))
    return neighbors

def bfs_1(map, x, y, c):
    q = deque([(x, y)])
    vis = set([(x, y)])
    a, p = 0, 0
    while q:
        x, y = q.popleft()
        if map[x][y][1] == 0:
            a += 1
            map[x][y] = (c, 1)
            ns = neigh(map, x, y, c)
            p += 4-len(ns)
            for nx, ny in ns:
                q.append((nx, ny))
                vis.add((nx, ny))
    return a * p

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    g = []
    for line in data:
        t = []
        for c in line:
            t.append((c, 0))
        g.append(t)
    s = 0

    for i, line in enumerate(g):
        for j, (c, v) in enumerate(line):
            if v == 0:
                s += bfs_1(g, i, j, c)
                # a, p = 0, 0
                # ns = neigh(data, i, j, c)
                # for (ni, nj) in ns:
                #     (nc, nv) = data[ni][nj]
                #     if nc == c and nv == 0:
                #         a += 1
                #         data[ni][nj] = (nc, 1)
                # p += 4 - len(ns)
    return s


def neigh_2(map, x, y, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
            neighbors.append((nx, ny))
    return neighbors


def bfs_2(map, x, y, c):
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    q = deque([(x, y)])
    vis = set()
    p = dict()
    a = 0
    while q:
            r2,c2 = q.popleft()
            if (r2,c2) in vis:
                continue
            vis.add((r2,c2))
            a += 1
            for dr,dc in dirs:
                rr = r2+dr
                cc = c2+dc
                if 0<=rr<len(map) and 0<=cc<len(map[0]) and map[rr][cc] == map[r2][c2]:
                    q.append((rr,cc))
                else:
                    if (dr,dc) not in p:
                        p[(dr,dc)] = set()
                    p[(dr,dc)].add((r2,c2))
    return p, a


aoc_helper.lazy_test(day=12, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    sc = 0

    vis = set()

    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if (i,j) in vis:
                continue


            q = deque([(i, j)])
            p = dict()
            a = 0
            while q:
                    r2,c2 = q.popleft()
                    if (r2,c2) in vis:
                        continue
                    vis.add((r2,c2))
                    a += 1
                    for dr,dc in dirs:
                        rr = r2+dr
                        cc = c2+dc
                        if 0<=rr<len(data) and 0<=cc<len(data[0]) and data[rr][cc] == data[r2][c2]:
                            q.append((rr,cc))
                        else:
                            if (dr,dc) not in p:
                                p[(dr,dc)] = set()
                            p[(dr,dc)].add((r2,c2))

            sides = 0
            for k,vs in p.items():
                s_p = set()
                old_sides = sides
                for (pr,pc) in vs:
                    if (pr,pc) not in s_p:
                        sides += 1
                        q = deque([(pr,pc)])
                        while q:
                            r2,c2 = q.popleft()
                            if (r2,c2) in s_p:
                                continue
                            s_p.add((r2,c2))
                            for dr,dc in dirs:
                                rr,cc = r2+dr,c2+dc
                                if (rr,cc) in vs:
                                    q.append((rr,cc))
            sc += a * sides
    return sc


aoc_helper.lazy_test(day=12, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2024, solution=part_two, data=data)
