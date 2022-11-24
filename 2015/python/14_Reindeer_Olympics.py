import re
from collections import Counter


def read_input():
    for line in open('14_input.txt'):
        name, speed, dur, rest = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line).groups()
        yield name, int(speed), int(dur), int(rest)


def calc(h, t):
    name, speed, dur, rest = h
    a, b = divmod(t, dur+rest)
    return a * dur * speed + (b * speed if b <= dur else dur * speed)


def simulate(horses, t):
    for i in range(1, t+1):
        tmp = {h[0]: calc(h, i) for h in horses}
        maxdist = max(tmp.values())
        yield from (k for k, v in tmp.items() if v == maxdist)


horses = list(read_input())
T = 2503
print('Star 1:', max(calc(h, T) for h in horses))
print('Star 2:', Counter(simulate(horses, T)).most_common()[0][1])