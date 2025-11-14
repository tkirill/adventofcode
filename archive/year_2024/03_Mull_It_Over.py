from aoc.io import *
import re


lines = readlines()

result = 0
for line in lines:
    for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', line):
        a, b = m.groups()
        result += int(a) * int(b)
print('Star 1:', result)

result = 0
enabled = True
for line in lines:
    for m in re.finditer(r'(do\(\))|(don\'t\(\))|(mul\((\d{1,3}),(\d{1,3})\))', line):
        match m.groups():
            case 'do()', _, _, _, _:
                enabled = True
            case _, 'don\'t()', _, _, _:
                enabled = False
            case _, _, _, a, b:
                if enabled:
                    result += int(a) * int(b)
print('Star 2:', result)