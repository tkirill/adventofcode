from aoc import *
import re
from collections import defaultdict


lines = readlines()
total = 0
gears = defaultdict(list)


def find_parts(row, match):
    for r in range(row - 1, row + 2):
        for c in range(match.start() - 1, match.end() + 1):
            if 0 <= r < len(lines) and 0 <= c < len(lines[row]):
                v = lines[r][c]
                if not v.isdigit() and v != ".":
                    yield r, c, v


for row, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        has_part = False
        number = int(match.group(0))
        for r, c, v in find_parts(row, match):
            has_part = True
            if v == "*":
                gears[(r, c)].append(number)
        if has_part:
            total += number
print("Star 1:", total)
print("Star 2:", sum(v[0] * v[1] for v in gears.values() if len(v) == 2))
