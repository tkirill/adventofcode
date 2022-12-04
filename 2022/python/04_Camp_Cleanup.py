from aoc import *


tasks = read(sep=',|-')

print('Star 1:', sum(a <= x <= y <= b or x <= a <= b <= y for a, b, x, y in tasks))
print('Star 2:', sum(a <= x <= b or x <= a <= y for a, b, x, y in tasks))