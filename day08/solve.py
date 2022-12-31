# solve file for day08 problem 
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from read_file import by_lines

solve_dir = path.dirname(path.abspath(__file__))
input_path = path.join(solve_dir, "input")
content = by_lines(input_path)
testcontent = '''30373
25512
65332
33549
35390'''.split("\n")

# generated by make_dirs.py

def part1() -> int:
    res = 0 
    grid = [[int(ch) for ch in line] for line in content]
    maxrow = len(grid)
    maxcol = len(grid[0])

    for i in range(maxrow):
        for j in range(maxcol):
            if visiable(grid, i, j):
                res += 1
    return res

from typing import List
def visiable(grid: List[List[int]], i: int, j: int) -> bool:
    if i == 0 or j == 0:
        return True
    if i == len(grid) - 1 or j == len(grid[0]) - 1:
        return True

    lower = lambda x : x < grid[i][j]

    # left visiable
    if all(map(lower, grid[i][:j])):
        return True
    # right visiable
    if all(map(lower, grid[i][j+1:])):
        return True
    # top visiable
    if all(map(lower, [row[j] for row in grid[:i]])):
        return True
    # bottom visiable
    if all(map(lower, [row[j] for row in grid[i+1:]])):
        return True

    return False

def part2() -> int:
    res = 0 
    grid = [[int(ch) for ch in line] for line in content]
    maxrow = len(grid)
    maxcol = len(grid[0])

    for i in range(1, maxrow-1):
        for j in range(1, maxcol-1):
            score = get_score(grid, i, j)
            res = max(res, score)

    return res

def get_score(grid: List[List[int]], row: int, col: int) -> int:
    up, down, left, right = 0, 0, 0, 0

    h = grid[row][col]

    for i in range(row-1, -1, -1):
        up += 1
        if grid[i][col] >= h:
            break
    
    for i in range(row+1, len(grid)):
        down += 1
        if grid[i][col] >= h:
            break
    
    for i in range(col-1, -1, -1):
        left += 1
        if grid[row][i] >= h:
            break
    
    for i in range(col+1, len(grid[0])):
        right += 1
        if grid[row][i] >= h:
            break

    return up * down * left * right

if __name__ == "__main__":
    print("part1", part1())
    print("part2", part2())
