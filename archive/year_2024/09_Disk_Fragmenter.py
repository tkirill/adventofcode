from aoc.io import *
import itertools as itls


disk_map = [int(x) for x in readlines()[0]]
disk = []
cur = itls.count()
for s, is_empty in zip(disk_map, itls.cycle([False, True])):
    disk.extend(['.' if is_empty else next(cur)] * s)


disk1 = list(disk)
write_pos = disk1.index('.')
for read_pos in range(len(disk1)-1, -1, -1):
    if disk1[read_pos] == '.':
        continue
    if read_pos < write_pos:
        break
    disk1[write_pos] = disk1[read_pos]
    disk1[read_pos] = '.'
    write_pos = disk1.index('.', write_pos)
print('Star 1:', sum(i*x for i, x in enumerate(disk1) if x != '.'))


disk2 = list(disk)
write_pos = disk2.index('.')
read_pos = len(disk2)-1
while True:
    if read_pos < 0:
        break
    for k, g in itls.groupby(range(read_pos, -1, -1), key=disk2.__getitem__):
        if k == '.':
            continue
        block = list(g)
        read_pos = block[-1] - 1
        for ek, eg in itls.groupby(range(write_pos, len(disk2)), key=disk2.__getitem__):
            if ek != '.':
                continue
            eblock = list(eg)
            if eblock[0] > block[0]:
                break
            if len(eblock) < len(block):
                continue
            min_len = min(len(block), len(eblock))
            disk2[eblock[0]:eblock[0]+min_len] = [k]*min_len
            disk2[block[-1]:block[0]+1] = ['.']*len(block)
            if disk2[write_pos] != '.':
                write_pos = disk2.index('.', write_pos+1)
            break
print('Star 2:', sum(i*x for i, x in enumerate(disk2) if x != '.'))