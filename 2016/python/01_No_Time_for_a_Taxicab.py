from aoc import *


directions = [(x[0], int(x[1:])) for x in read(sep=', ')[0]]
print('Star 1:', ComplexWalker().walkall(directions).mdist())

walker = ComplexWalker()
visited = {walker.pos}
for nxt in walker.walk_by1(directions):
    if nxt.pos in visited:
        print('Star 2:', nxt.mdist())
        break
    visited.add(nxt.pos)


directions = [(x[0], int(x[1:])) for x in read(sep=', ')[0]]
print('Star 1:', Walker2d().walkall(directions).mdist())

walker = Walker2d()
visited = {walker.pos}
for nxt in walker.walk_by1(directions):
    if nxt.pos in visited:
        print('Star 2:', nxt.mdist())
        break
    visited.add(nxt.pos)