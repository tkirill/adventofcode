from functools import cache

containers = [int(l) for l in open('17_input.txt')]
containers.sort()

comb_150 = set()

@cache
def cntall(visited, total, n):
    if total == 150:
        comb_150.add((visited, n))
        return
    if total > 150:
        return
    
    for i in range(len(containers)):
        mask = 1 << i
        if visited & mask:
            continue
        visited |= mask
        cntall(visited, total + containers[i], n+1)
        visited ^= mask

cntall(0, 0, 0)
print('Star 1:', len(comb_150))
minc = min(c for _, c in comb_150)
print('Star 2:', sum(1 for _, c in comb_150 if c == minc))


# Brute force from reddit

from itertools import combinations

q1, q2 = 0, 0
for i in range(1, len(containers)+1):
    for c in combinations(containers, i):
        if sum(c) == 150:
            q1 += 1
    if q1 and not q2:
        q2 = q1
print('Star 1:', q1)
print('Star 2:', q2)