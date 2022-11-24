from itertools import groupby


cur = open('10_input.txt').readline().strip()
for i in range(50):
    if i == 41:
        print('Star 1:', len(cur))
    cur = ''.join(f'{sum(1 for _ in g)}{c}' for c, g in groupby(cur))
print('Star 2:', len(cur))