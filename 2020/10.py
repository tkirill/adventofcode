from collections import Counter
from functools import cache


def star1():
    adapters = [0] + sorted(int(s.strip()) for s in open('input.txt'))
    adapters.append(adapters[-1] + 3)
    c = Counter(adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1))
    print(c[1] * c[3])


def star2():
    adapters = [int(s.strip()) for s in open('input.txt')]
    adapters.append(0)
    adapters.sort()

    @cache
    def count(pos):
        return 1 if pos == len(adapters) - 1 else sum(
            count(next_pos) for next_pos in range(pos + 1, min(len(adapters), pos + 4)) if
            adapters[next_pos] - adapters[pos] <= 3)

    print(count(0))


print('Star 1:')
star1()
print('Star 2:')
star2()