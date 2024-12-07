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
import tqdm

raw = aoc_helper.fetch(7, 2024)


def parse_raw(raw: str):
    return [re.findall(r"\d+", row) for row in raw.splitlines()]


data = parse_raw(raw)

def solve_1(answer, sum, values):
    if values == []:
        return sum
    else:
        next = values.pop(0)
        add_ans = solve_1(answer, sum + next, deepcopy(values))
        if add_ans == answer:
            return add_ans
        mul_ans = solve_1(answer, sum * next, deepcopy(values))
        if mul_ans == answer:
            return mul_ans

def solve_2(answer, sum, values):
    if values == []:
        return sum
    else:
        next = values.pop(0)
        add_ans = solve_2(answer, sum + next, deepcopy(values))
        if add_ans == answer:
            return add_ans
        mul_ans = solve_2(answer, sum * next, deepcopy(values))
        if mul_ans == answer:
            return mul_ans
        concat_ans = solve_2(answer, int(str(sum) + str(next)), deepcopy(values))
        if concat_ans == answer:
            return concat_ans
    

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = 0
    for row in tqdm.tqdm(data):
        answer = int(row.pop(0))
        if solve_1(answer, 0, list(map(int, row))) == answer:
            score += answer
    return score


aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    for row in tqdm.tqdm(data):
        answer = int(row.pop(0))
        if solve_2(answer, 0, list(map(int, row))) == answer:
            score += answer
    return score


aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2024, solution=part_two, data=data)
