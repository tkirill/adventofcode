from aoc.io import *


elfs = [sum(x) for x in readblocks()]
elfs.sort()

print('Star 1:', elfs[-1])
print('Star 2:', sum(elfs[-3:]))