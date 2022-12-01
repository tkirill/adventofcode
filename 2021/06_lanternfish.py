# https://adventofcode.com/2021/day/6
from utils import *
from collections import deque


def read_input(days):
    fishes = deque([0]*9)
    for x in read('6_input.txt'):
        fishes[x] += 1
    for _ in range(days):
        fishes.rotate(-1)
        fishes[6] += fishes[8]
    return sum(fishes)


print('Star 1:', read_input(80))
print('Star 2:', read_input(256))