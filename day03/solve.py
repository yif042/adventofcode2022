# solve file for day03 problem
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from read_file import by_lines
solve_dir = path.dirname(path.abspath(__file__))
input_path = path.join(solve_dir, "input")
content = by_lines(input_path)

# generated by make_dirs.py

a_z = list(map(chr, range(ord("a"), ord("z")+1)))
A_Z = list(map(chr, range(ord("A"), ord("Z")+1)))
priorities = {ch: (i + 1) for i, ch in enumerate(a_z + A_Z)}


def part1():
    res = 0
    for l in content:
        counterpart = len(l) // 2
        first, second = l[counterpart:], l[:counterpart]

        res += get_priority(first, second)

    print("part1", res)
    


def get_priority(first: str, second: str) -> int:
    firstset = set(list(first))
    for ch in second:
        if ch in firstset:
            # print(ch, first, second)
            return priorities[ch]

    raise ValueError("no same character")


part1()




