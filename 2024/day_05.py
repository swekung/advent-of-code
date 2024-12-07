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

raw = aoc_helper.fetch(5, 2024)


def parse_raw(raw: str):
    data = raw.split("\n\n")
    rules = []
    for rule in data[0].splitlines():
        rules.append(re.findall(r"\d+", rule))
    updates = []
    for update in data[1].splitlines():
        updates.append(re.findall(r"\d+", update))
    return (rules, updates)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    rules, updates = data
    score = 0
    
    for update in updates:
        valid = True
        for (i, page) in enumerate(update):
            for rule in rules:
                if page in rule[0]: # check if page appears after
                    tmp = rule[1]
                    if tmp in update[:i]:
                        valid = False
                if page in rule[1]:
                    tmp = rule[0]
                    if tmp in update[i:]:
                        valid = False
        if valid:
            score += int(update[int(len(update)/2)])
    return score
                    



aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    rules, updates = data
    score = 0
    invalids = []
    
    for update in updates:
        valid = True
        for (i, page) in enumerate(update):
            for rule in rules:
                if page in rule[0]: # check if page appears after
                    tmp = rule[1]
                    if tmp in update[:i]:
                        valid = False
                if page in rule[1]:
                    tmp = rule[0]
                    if tmp in update[i:]:
                        valid = False
        if not valid:
            invalids.append(update)
    
    sorts = []
    for update in invalids:
        sorted_update = []
        for page in update:
            inserted = False
            min_index, max_index = -1, len(sorted_update) +1
            for rule in rules:
                if page in rule[1]:
                    tmp = rule[0]
                    if tmp in sorted_update:
                        if sorted_update.index(tmp) >= min_index:
                            min_index = sorted_update.index(tmp) + 1
                        
                elif page in rule[0]:
                    tmp = rule[1]
                    if tmp in sorted_update:
                        if sorted_update.index(tmp) < max_index:
                            max_index = sorted_update.index(tmp)
                        
            if min_index != -1:
                sorted_update.insert(min_index, page)
            else:
                sorted_update.insert(max_index, page)
        score += int(sorted_update[int(len(sorted_update)/2)])
        sorts.append(sorted_update)

    
    return score




aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2024, solution=part_two, data=data)
