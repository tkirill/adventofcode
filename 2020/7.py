import re
from collections import defaultdict


def read_input():
    graph = defaultdict(list)
    for line in open('input.txt'):
        line = line.strip()
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        bag, contain = line.split(' bags contain ')
        if 'no other' in contain:
            graph[bag] = []
            continue
        for item in contain.split(', '):
            m = re.match('(\d)+ (.+?) bag', item)
            n, child_bag = m.group(1), m.group(2)
            graph[bag].append((child_bag, int(n)))
    return graph


def count_parents(graph):
    parents = 0
    q = list()
    visited = set()
    start = 'shiny gold'

    q.append(start)
    visited.add(start)
    while q:
        cur = q.pop()
        for bag in graph:
            if bag not in visited and any(cur == req for req, n in graph[bag]):
                parents += 1
                visited.add(bag)
                q.append(bag)
    return parents


def star1():
    graph = read_input()
    print(count_parents(graph))


def count_children(graph):
    children = 0
    q = list()
    start = 'shiny gold'

    q.append((start, 1))
    while q:
        cur, cur_n = q.pop()
        for bag_info in graph[cur]:
            bag, n = bag_info
            children += n * cur_n
            q.append((bag, n * cur_n))
    return children


def star2():
    graph = read_input()
    print(count_children(graph))


print('Star 1:')
star1()
print('Star 2:')
star2()