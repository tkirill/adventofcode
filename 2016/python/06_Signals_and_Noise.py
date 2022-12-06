from aoc import *
from collections import Counter


rows = read()
counters = [Counter(c) for c in columns(rows)]

print('Star 1:', ''.join(c.most_common()[0][0] for c in counters))
print('Star 2:', ''.join(c.most_common()[-1][0] for c in counters))