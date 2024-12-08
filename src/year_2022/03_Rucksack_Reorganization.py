from aoc.io import *
from aoc import algo


rucksacks = read()


total = 0
for r in rucksacks:
    h1, h2 = r[:len(r)//2], r[len(r)//2:]
    common = (set(h1) & set(h2)).pop()
    total += algo.asciipos(common) + 1 + int(common.isupper()) * 26

print('Star 1:', total)


total = 0
for i in range(0, len(rucksacks), 3):
    sets = list(map(set, rucksacks[i:i+3]))
    common = list(sets[0] & sets[1] & sets[2])[0]
    total += algo.asciipos(common) + 1 + int(common.isupper()) * 26

print('Star 2:', total)