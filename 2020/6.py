import re
import string


def read_groups():
    cur = []
    for line in open('input.txt'):
        line = line.strip()
        if not line:
            yield cur
            cur = []
            continue
        cur.append(line)
    yield cur


def count_all_yes1(group):
    count = 0
    for alpha in string.ascii_lowercase:
        if any(alpha in line for line in group):
            count += 1
    return count


def star1():
    print(sum(count_all_yes1(g) for g in read_groups()))


def count_all_yes2(group):
    count = 0
    for alpha in string.ascii_lowercase:
        if all(alpha in line for line in group):
            count += 1
    return count


def star2():
    print(sum(count_all_yes2(g) for g in read_groups()))


print('Star 1:')
star1()
print('Star 2:')
star2()