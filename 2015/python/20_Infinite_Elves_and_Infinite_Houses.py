from math import sqrt, ceil
from itertools import count

at_least = int(open('20_input.txt').readline())
LIMIT = at_least // 40

houses = [0]*(LIMIT+1)
for i in range(1, LIMIT):
    for j in range(i, LIMIT, i):
        houses[j] += i*10
print('Star 1:', next(i for i in range(len(houses)) if houses[i] >= at_least))

houses = [0]*(LIMIT+1)
for i in range(1, LIMIT):
    for j in range(i, min(i*50, LIMIT), i):
        houses[j] += i*11
print('Star 2:', next(i for i in range(len(houses)) if houses[i] >= at_least))