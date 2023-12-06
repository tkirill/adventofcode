from aoc import *


def multiply_wins(times, dists):
    total = 1
    for time, dist in zip(times, dists):
        curtotal = 0
        for i in range(time):
            curdist = (time - i) * i
            if curdist > dist:
                curtotal += 1
        if curtotal:
            total *= curtotal
    return total


lines = read(sep=": +| +")
print("Star 1:", multiply_wins(lines[0][1:], lines[1][1:]))
time = int("".join(str(x) for x in lines[0][1:]))
dist = int("".join(str(x) for x in lines[1][1:]))
print("Star 2:", multiply_wins([time], [dist]))
