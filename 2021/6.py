from utils import *
from collections import deque


def read_input(days):
    fishes = deque([0]*9)
    for x in parse1d(readlines('6_input.txt')[0], ','):
        fishes[x] += 1
    for _ in range(days):
        fishes.rotate(-1)
        fishes[6] += fishes[8]
    return sum(fishes)


print('Star 1:', read_input(80))
print('Star 2:', read_input(256))