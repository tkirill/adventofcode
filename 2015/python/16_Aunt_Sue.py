import re


TGT = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}


def read_input():
    for l in open('16_input.txt'):
        l = l.strip()
        suen, an = re.match(r'Sue (\d+): (.+)', l).groups()
        animals = {m.group(1): int(m.group(2)) for m in re.finditer(r'(\w+): (\d+)', an)}
        yield suen, animals


sues = list(read_input())


def is_ok(s, t):
    for k, v in t.items():
        if k in s[1] and s[1][k] != v:
            return False
    return True


def real_is_ok(s, t):
    for k, v in t.items():
        if k in s[1]:
            if k in ['cats', 'trees']:
                if s[1][k] <= v:
                    return False
            elif k in ['pomeranians', 'goldfish']:
                if s[1][k] >= v:
                    return False
            elif s[1][k] != v:
                return False
    return True


print('Star 1:', next(s for s in sues if is_ok(s, TGT))[0])
print('Star 2:', next(s for s in sues if real_is_ok(s, TGT))[0])