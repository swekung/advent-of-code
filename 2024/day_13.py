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
from ortools.linear_solver import pywraplp

raw = aoc_helper.fetch(13, 2024)


def parse_raw(raw: str):
    c = raw.split("\n\n")
    out = []
    for line in c:
        out.append([int(x) for x in re.findall(r"[\+-]*\d+", line)])
    return out

data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    score = 0
    cost_a = 3
    cost_b = 1
    for a_x, a_y, b_x, b_y, t_x, t_y in data:
        max_n_A = t_x // a_x if a_x != 0 else t_y // a_y
        min_cost = float('inf')
        for n_A in range(max_n_A + 1):
            rem_x = t_x - n_A * a_x
            rem_y = t_y - n_A * a_y

            if rem_x >= 0 and rem_y >= 0 and (rem_x % b_x == 0) and (rem_y % b_y == 0):
                n_B = rem_x // b_x
                if n_B * b_y == rem_y:
                    cost = 3 * n_A + n_B
                    if cost < min_cost:
                        min_cost = cost
                        best_combo = (n_A, n_B)

        score += min_cost if min_cost != float('inf') else 0
    return score



aoc_helper.lazy_test(day=13, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    score = 0
    cost_a = 3
    cost_b = 1
    for a_x, a_y, b_x, b_y, t_x, t_y in data:
        t_x += 10000000000000
        t_y += 10000000000000

        solver = pywraplp.Solver.CreateSolver('SCIP')
        if not solver:
            return None, None

        n_A = solver.IntVar(0, solver.infinity(), 'n_A')
        n_B = solver.IntVar(0, solver.infinity(), 'n_B')

        solver.Add(n_A * a_x + n_B * b_x == t_x)
        solver.Add(n_A * a_y + n_B * b_y == t_y)


        solver.Minimize(3 * n_A + n_B)

        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            min_cost = solver.Objective().Value()
            solution = {
                "n_A": int(n_A.solution_value()),
                "n_B": int(n_B.solution_value())
            }
            score += min_cost



        #score += min_cost if min_cost != float('inf') else 0
    return int(score)


aoc_helper.lazy_test(day=13, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=13, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=13, year=2024, solution=part_two, data=data)
