from collections import Counter, defaultdict, deque
import heapq


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

raw = aoc_helper.fetch(9, 2024)


def parse_raw(raw: str):
    return [int(c) for c in raw]


data = parse_raw(raw)

def check_fill(disk):
    num = False
    for i in range(len(disk) - 1, 0, -1):
        if disk[i][0] == "." and num:
            return False
        else:
            num = True
    return True

def print_disk(disk):
    sum = 0
    pos = 0
    out = ""
    for c in disk:
        for i in range(c[1]):
            out += str(c[0])
            pos += 1
    print(out)

def fill_1(disk):

    while not check_fill(disk):
        while disk[-1][0] == ".":
            disk.pop(-1)
        for i, c in enumerate(disk):
            if c[0] == ".":
                size = c[1]
                last = disk[-1]
                if last[1] > size:
                    disk[-1] = (last[0], last[1] - size)
                    disk[i] = (last[0], size)
                else:
                    disk.pop(-1)
                    disk[i] = (last[0], last[1])
                    disk.insert(i + 1, (".", size - last[1]))
                break
    return disk


def calc_checksum(disk):
    sum = 0
    pos = 0
    out = ""
    for c in disk:
        for i in range(c[1]):
            if c[0] != ".":
                sum += c[0] * pos
            out += str(c[0])
            pos += 1
    return sum




# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    pos = 0
    ch = 0
    id = 0
    em = False
    disk = []
    for c in data:
        if em:
            if c != 0:
                disk.append((".", c))
            pos += c
            em = False
        else:
            disk.append((id, c))
            id += 1
            em = True
    fill_1(disk)
    return calc_checksum(disk)



aoc_helper.lazy_test(day=9, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    lengths = data
    filled_grid = {}
    gaps = defaultdict(lambda: [])

    cur_pos = 0
    for i,num in enumerate(lengths):
        if i%2 == 0:
            filled_grid[i//2] = [cur_pos,num]
        else:
            if num > 0:
                heapq.heappush(gaps[num],cur_pos)
        cur_pos += num

    for i in sorted(filled_grid.keys(),reverse=True):
        file_start_pos,file_len = filled_grid[i]
        possible_gaps = sorted([[gaps[gap_len][0],gap_len] for gap_len in gaps if gap_len>=file_len])
        if possible_gaps:
            gap_start_pos,gap_len = possible_gaps[0]
            if file_start_pos > gap_start_pos:
                filled_grid[i] = [gap_start_pos,file_len]
                remaining_gap_len = gap_len-file_len
                heapq.heappop(gaps[gap_len])
                if not gaps[gap_len]:
                    del gaps[gap_len]
                if remaining_gap_len:
                    heapq.heappush(gaps[remaining_gap_len],gap_start_pos+file_len)
                    
    answer = sum(num*(start*length+(length*(length-1))//2) for num,(start,length) in filled_grid.items())
    return answer

with open("input.txt", "r") as f:
    data = [int(x) for x in f.read()]
    print(part_two(data))


aoc_helper.lazy_test(day=9, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2024, solution=part_two, data=data)
