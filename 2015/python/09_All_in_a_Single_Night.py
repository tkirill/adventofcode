from collections import defaultdict
import operator


def build_graph(lines: list[str]) -> dict[list[str]]:
    g = defaultdict(list)
    for line in lines:
        src, _, dst, _, wstr = line.split()
        g[src].append((dst, int(wstr)))
        g[dst].append((src, int(wstr)))
    return g


lines = [l.strip() for l in open('09_input.txt')]
g = build_graph(lines)

def visitall(cur: str, visited: set[str], cost: int, cmp) -> int:
    if len(visited) == len(g):
        return cost
    mincost = None
    for nbgh, w in g[cur]:
        if nbgh in visited:
            continue
        visited.add(nbgh)
        tmp = visitall(nbgh, visited, cost+w, cmp)
        if tmp is not None and (mincost is None or cmp(tmp, mincost)):
            mincost = tmp
        visited.remove(nbgh)
    return mincost

print('Star 1:', min(visitall(x, {x}, 0, operator.lt) or 1000*1000 for x in g))
print('Star 2:', max(visitall(x, {x}, 0, operator.gt) or 1000*1000 for x in g))