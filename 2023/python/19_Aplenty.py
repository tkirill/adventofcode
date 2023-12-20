from __future__ import annotations
from aoc import *
import re
import abc


class StatementABC(abc.ABC):
    outcome: str

    def __call__(self, x: dict) -> str:
        ...

    def intersect_range(self, ranges: dict[str, Range]) -> dict[str, Range]:
        ...

    def invert(self) -> StatementABC:
        ...


class ComparisonABC(abc.ABC):
    range: Range

    def invert(self) -> ComparisonABC:
        ...


@dataclass
class LessThan(ComparisonABC):
    val: int

    def __post_init__(self):
        self.range = Range(-1_000_000_000, self.val - 1)

    def invert(self):
        return GreaterThan(self.val - 1)


@dataclass
class GreaterThan(ComparisonABC):
    val: int

    def __post_init__(self):
        self.range = Range(self.val + 1, 1_000_000_000)

    def invert(self):
        return LessThan(self.val + 1)


@dataclass
class IfStatement(StatementABC):
    category: str
    comparison: ComparisonABC
    outcome: str

    def __call__(self, x: dict) -> str | None:
        if self.category in x and x[self.category] in self.comparison.range:
            return self.outcome
        return None

    def intersect_range(self, ranges: dict[str, Range]) -> dict[str, Range]:
        tmp = dict(ranges)
        tmp[self.category] = tmp[self.category].intersect(self.comparison.range)
        return tmp

    def invert(self) -> IfStatement:
        return IfStatement(self.category, self.comparison.invert(), self.outcome)

    @classmethod
    def parse(cls, s: str) -> IfStatement:
        cmp, outcome = s.split(":")
        category, op, val = cmp[0], cmp[1], cmp[2:]
        val = int(val)
        cmp = LessThan(val) if op == "<" else GreaterThan(val)
        return IfStatement(category, cmp, outcome)


@dataclass
class ConstantStatement(StatementABC):
    outcome: str

    def __call__(self, x: dict) -> str:
        return self.outcome

    def intersect_range(self, ranges: dict[str, Range]) -> dict[str, Range]:
        return ranges

    def invert(self) -> ConstantStatement:
        return self


@dataclass
class Workflow:
    name: str
    statements: dict[StatementABC]

    def __call__(self, x: dict) -> str:
        for s in self.statements:
            tmp = s(x)
            if tmp is not None:
                return tmp
        raise Exception()

    @classmethod
    def parse(cls, line: str) -> Workflow:
        name, spec = re.match("^([a-z]+){(.+)}$", line).groups()
        *statements, default = spec.split(",")
        tmp = [IfStatement.parse(s) for s in statements]
        tmp.append(ConstantStatement(default))
        return Workflow(name, tmp)


def parse_part(s: str) -> dict:
    i = allints(s)
    return {"x": i[0], "m": i[1], "a": i[2], "s": i[3]}


wlines, plines = readblocks()
workflows = [Workflow.parse(s) for s in wlines]
workflows = {w.name: w for w in workflows}
parts = [parse_part(s) for s in plines]


total = 0
for p in parts:
    cur = "in"
    while cur not in ["A", "R"]:
        cur = workflows[cur](p)
    if cur == "A":
        total += sum(p.values())
print("Star 1:", total)


total = 0


def dfs_workflows(cur, cur_ranges: dict[str, Range]):
    global total
    if cur == "A":
        tmp = 1
        for r in cur_ranges.values():
            tmp *= len(r)
        total += tmp
        return
    if cur == "R":
        return
    for s in workflows[cur].statements:
        dfs_workflows(s.outcome, s.intersect_range(cur_ranges))
        cur_ranges = s.invert().intersect_range(cur_ranges)


dfs_workflows("in", {k: Range(1, 4000) for k in "xmas"})
print("Star 2:", total)
