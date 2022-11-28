from collections import defaultdict
import re


def read_input():
    rules = defaultdict(list)
    for l in open('19_input.txt'):
        l = l.strip()
        if '=>' in l:
            s, d = l.split(' => ')
            rules[s].append(d)
        elif not l:
            continue
        else:
            return rules, l


def replaceall(rules, x: str):
    mem = set()
    for s, rpls in rules.items():
        for r in rpls:
            for m in re.finditer(s, x):
                mem.add(x[:m.start()] + r + x[m.end():])
    return mem


rls, start = read_input()
print('Star 1:', len(replaceall(rls, start)))


rls2 = [(dst, src) for src, rplcs in rls.items() for dst in rplcs]
rls2.sort(key=lambda x: -len(x[0]))


def replaceone(cur):
    for s, d in rls2:
        m = list(re.finditer(s, cur))
        if m:
            print(s, d)
            return cur[:m[-1].start()] + d + cur[m[-1].end():], True
    return cur, False


def findminrplcs(cur):
    steps = 0
    while cur != 'e':
        tmp, done = replaceone(cur)
        if done:
            cur = tmp
            steps += 1
    return steps


print('Star 2:', findminrplcs(start))