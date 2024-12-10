from aoc.io import *
from collections import defaultdict


cmds = readlines()
sizes = defaultdict(int)
curpath = []
joinpath = lambda: '/'.join(curpath)

for cmd in cmds:
    if cmd == '$ cd ..':
        tmp = joinpath()
        curpath.pop()
        sizes[joinpath()] += sizes[tmp]
        continue
    if cmd.startswith('$ cd'):
        curpath.append(cmd.split()[-1])
        continue
    size = allints(cmd)
    if size:
        sizes[joinpath()] += size[0]
        continue
while curpath:
    tmp = joinpath()
    curpath.pop()
    sizes[joinpath()] += sizes[tmp]

print('Star 1:', sum(x for x in sizes.values() if x <= 100000))
space_needed = 30000000 - (70000000 - sizes['/'])
print('Star 2:', next(x for x in sorted(sizes.values()) if x >= space_needed))


### Alternative solution with recursion ###


cmds = readlines()
sizes = dict()


def readdir(curpath, ip):
    total = 0
    while ip < len(cmds):
        cmd = cmds[ip]
        if cmd == '$ cd ..':
            ip += 1
            break
        if cmd.startswith('$ cd'):
            curpath.append(cmd.split()[-1])
            subsize, ip = readdir(curpath, ip+1)
            total += subsize
            curpath.pop()
            continue
        size = allints(cmd)
        if size:
            total += size[0]
        ip += 1
    sizes['/'.join(curpath)] = total
    return total, ip


readdir([], 0)
print('Star 1 (recursion):', sum(x for x in sizes.values() if x <= 100000))
space_needed = 30000000 - (70000000 - sizes['/'])
print('Star 2 (recursion):', next(x for x in sorted(sizes.values()) if x >= space_needed))