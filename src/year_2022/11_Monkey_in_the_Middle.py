from __future__ import annotations
from aoc.io import *
from dataclasses import dataclass
import math


@dataclass
class Monkey:
    items: list[int]
    op: str
    test: int
    if_true: int
    if_false: int

    def evalop(self, old: int) -> int:
        return eval(self.op, None, {'old': old})


def read_input():
    blocks = readblocks(sep=None)
    monkeys = []
    globalmod = math.lcm(*[allints(b[3])[0] for b in blocks])


    for monkey in blocks:
        items = allints(monkey[1])
        op = monkey[2].split(' = ')[-1]
        test = allints(monkey[3])[0]
        if_true = allints(monkey[4])[-1]
        if_false = allints(monkey[5])[-1]

        pt = parseline(op)
        if isinstance(pt[2], int):
            pt[2] %= globalmod
            pt[2] = str(pt[2])
        op = ' '.join(pt)
        for i in range(len(items)):
            items[i] %= globalmod
        
        monkeys.append(Monkey(items, op, test, if_true, if_false))
    return monkeys, globalmod


def run(monkeys: list[Monkey], modify_item: Callable[[int], int]):
    totals = [0] * len(monkeys)
    for i, monkey in enumerate(monkeys):
        totals[i] += len(monkey.items)
        for item in monkey.items:
            new_item = modify_item(monkey.evalop(item))
            pass_to = monkey.if_false if new_item % monkey.test else monkey.if_true
            monkeys[pass_to].items.append(new_item)
        monkey.items.clear()
    return totals


def runmany(monkeys: list[Monkey], n: int, modify_item: Callable[[int], int]):
    totals = [0] * len(monkeys)
    for _ in range(n):
        tmp = run(monkeys, modify_item)
        for i, v in enumerate(tmp):
            totals[i] += v
    return totals
            
            

monkeys, globalmod = read_input()
totals = runmany(monkeys, 20, lambda x: x // 3)
totals.sort()
print('Star 1:', totals[-1] * totals[-2])


monkeys, common = read_input()
totals = runmany(monkeys, 10*1000, lambda x: x % globalmod)
totals.sort()
print('Star 2:', totals[-1] * totals[-2])