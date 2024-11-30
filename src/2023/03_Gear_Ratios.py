from aoc.io import *
from aoc import grid
import re
from collections import defaultdict


schematic = grid.Field(readlines())
total = 0
gears = defaultdict(list)


for row, s in enumerate(schematic.items):
    for m in re.finditer(r'\d+', s):
        number = int(m.group(0))
        has_part = False
        r = grid.Rectangle.ylr(row, m.start(), m.end()-1)
        for pos, v in schematic.insidev(grid.screen.near8_rectangle(r)):
            if not v.isdigit() and v != '.':
                has_part = True
            if v == '*':
                gears[pos].append(number)
        if has_part:
            total += number
print("Star 1:", total)
print("Star 2:", sum(v[0] * v[1] for v in gears.values() if len(v) == 2))