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
import regex as re
from copy import deepcopy
from z3 import *
from ortools.linear_solver import pywraplp

raw = aoc_helper.fetch(17, 2024)


def parse_raw(raw: str):
    raw = raw.split("\n\n")

    reg = []
    for line in raw[0].splitlines():
        reg.append(extract_ints(line)[0])
    
    ops = extract_ints(raw[1])
    return reg, ops


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    reg, ops = data
    out = []
    ptr = 0

    def op_conv(op):
        if 0 <= op <= 3:
            return op
        if op == 4:
            return reg[0]
        if op == 5:
            return reg[1]
        if op == 6:
            return reg[2]
    
    def op_adv(a, ptr):
        ptr += 2
        den = 2 ** op_conv(a)
        reg[0] =  int(reg[0] / den)
        return ptr
    
    def op_bxl(a, ptr):
        ptr += 2
        reg[1] =  a ^ reg[1]
        return ptr
    
    def op_bst(a, ptr):
        ptr += 2
        reg[1] =  op_conv(a) % 8
        return ptr
    
    def op_jnz(a, ptr):
        if reg[0] != 0:
            ptr = a
        else:
            ptr += 2
        return ptr
    
    def op_bxc(a, ptr):
        ptr += 2
        reg[1] = reg[1] ^ reg[2]
        return ptr
    
    def op_out(a, ptr):
        ptr += 2
        out.append(op_conv(a) % 8)
        return ptr
    
    def op_bdv(a, ptr):
        ptr += 2
        den = 2 ** op_conv(a)
        reg[1] =  int(reg[0] / den)
        return ptr
    
    def op_cdv(a, ptr):
        ptr += 2
        den = 2 ** op_conv(a)
        reg[2] =  int(reg[0] / den)
        return ptr
    
    while ptr < len(ops):
        op = ops[ptr]
        if op == 0:
            ptr = op_adv(ops[ptr + 1], ptr)
        elif op == 1:
            ptr = op_bxl(ops[ptr + 1], ptr)
        elif op == 2:
            ptr = op_bst(ops[ptr + 1], ptr)
        elif op == 3:
            ptr = op_jnz(ops[ptr + 1], ptr)
        elif op == 4:
            ptr = op_bxc(ops[ptr + 1], ptr)
        elif op == 5:
            ptr = op_out(ops[ptr + 1], ptr)
        elif op == 6:
            ptr = op_bdv(ops[ptr + 1], ptr)
        elif op == 7:
            ptr = op_cdv(ops[ptr + 1], ptr)

    out_str = ",".join(map(str, out))
    return out_str



aoc_helper.lazy_test(day=17, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    reg, ops = data
    reg[0] = 0

    def run(a):
        ip = 0
        abc = [a, 0, 0]

        def combo(n):
            if n < 4:
                return n
            else:
                return abc[n - 4]

        p1 = []
        while ip < len(ops):
            match ops[ip]:
                case 0:
                    abc[0] = abc[0] >> combo(ops[ip+1])
                case 1:
                    abc[1] ^= ops[ip+1]
                case 2:
                    abc[1] = combo(ops[ip+1]) & 7
                case 3:
                    if abc[0] != 0:
                        ip = ops[ip+1]
                        continue
                case 4:
                    abc[1] ^= abc[2]
                case 5:
                    p1.append(combo(ops[ip+1]) & 7)
                case 6:
                    abc[1] = abc[0] >> combo(ops[ip+1])
                case 7:
                    abc[2] = abc[0] >> combo(ops[ip+1])
                case _:
                    print('unknown opcode')
            ip += 2

        return p1


    steps = []
    for a in range(2 ** 10):
        steps.append(run(a)[0])


    ll = [[i] for i in range(2 ** 10) if steps[i] == ops[0]]


    for k in ops[1:]:
        ll_ = []
        for l in ll:
            current = l[-1] >> 3
            for i in range(8):
                if steps[(i << 7) + current] == k:
                    ll_.append(l + [(i << 7) + current])

        ll = ll_

    def recombine(l):
        i = l[0]
        d = 10

        for c in l[1:]:
            i += (c >> 7) << d
            d += 3

        return i

    ans = float('inf')
    for l in ll:
        i = recombine(l)
        if run(i) == ops:
            ans = min(i, ans)
    return ans




aoc_helper.lazy_test(day=17, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=17, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=17, year=2024, solution=part_two, data=data)
