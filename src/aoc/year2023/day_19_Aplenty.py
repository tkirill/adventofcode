from itertools import batched
import re
import dataclasses

from aoc.io import readblocks, allints


@dataclasses.dataclass
class Rule:
    
    categories: list[tuple[str, str, int, str]]
    default: str


def parse_rules(items: list[str]) -> dict[str, Rule]:
    rules = dict()
    for item in items:
        name, *rate_rules, default = re.split(r'[\{\},:]', item)[:-1]
        categories = []
        for condition, result in batched(rate_rules, 2):
            category, op, value = condition[0], condition[1], condition[2:]
            categories.append((category, op, int(value), result))
        rules[name] = Rule(categories, default)
    return rules


def parse_parts(items: list[str]) -> list[dict[str, int]]:
    result = []
    for item in items:
        x, m, a, s = allints(item)
        result.append({'x': x, 'm': m, 'a': a, 's': s})
    return result


def eval_rule(rule: Rule, part: dict[str, int]) -> tuple[str, bool]:
    for category, op, value, result in rule.categories:
        actual = part.get(category, None)
        if actual is None:
            continue
        if op == '<' and actual < value or op == '>' and actual > value:
            return result, False
    return rule.default, True


def eval_rules(rules: dict[str, Rule], part: dict[str, int]) -> bool:
    cur = 'in'
    while cur not in ['A', 'R']:
        cur, _ = eval_rule(rules[cur], part)
    return True if cur == 'A' else False



def star1():
    blocks = readblocks(2023, 19, sep=None, parse=str)
    rules, parts = parse_rules(blocks[0]), parse_parts(blocks[1])
    return sum(sum(p.values()) for p in parts if eval_rules(rules, p))


def star2():
    pass
