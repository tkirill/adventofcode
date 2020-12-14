import re
from itertools import product


def apply_to_val(mask, val):
    for i, bit in enumerate(reversed(mask)):
        if bit == 'X':
            continue
        if bit == '0':
            val &= ~(1 << i)
        else:
            val |= 1 << i
    return val


def star1():
    mem = dict()
    mask = None
    for line in open('input.txt'):
        line = line.strip()
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            m = re.match("mem\[(\d+)\] = (\d+)", line)
            n, val = m.group(1), int(m.group(2))
            mem[n] = apply_to_val(mask, val)
    print(sum(mem.values()))


def apply_to_mem(mask, n):
    t = []
    for i, bit in enumerate(reversed(mask)):
        if bit == 'X':
            t.append(['0', '1'])
        elif bit == '0':
            t.append([str((n & (1 << i)) >> i)])
        else:
            t.append(['1'])
    for tup in product(*t):
        yield ''.join(reversed(tup))


def star2():
    mem = dict()
    mask = None
    for line in open('input.txt'):
        line = line.strip()
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            m = re.match("mem\[(\d+)\] = (\d+)", line)
            n, val = int(m.group(1)), int(m.group(2))
            for x in apply_to_mem(mask, n):
                mem[x] = val
    print(sum(mem.values()))


print('Star 1:')
star1()
print('Star 2:')
star2()