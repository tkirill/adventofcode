from aoc import *


def dig_edge(steps: Iterable[tuple[str, int, str]]) -> list[Vec2]:
    return list(scanl(lambda pos, step: pos.step(step[0], step[1]), Vec2(), steps))


def dig_edge_hex(steps: Iterable[tuple[str, int, str]]) -> list[Vec2]:
    vertices = [Vec2()]
    for _, _, color in steps:
        hdist, dcode = color[2:7], color[7]
        dist, dir = int(hdist, base=16), 'RDLU'[int(dcode)]
        vertices.append(vertices[-1].step(dir, dist))
    return vertices


def dig_lagoon(vertices: list[Vec2]):
    delta = Vec2(min(v.x for v in vertices), min(v.y for v in vertices))
    area = 0
    edge = 0

    for i in range(1, len(vertices)):
        prev = vertices[i-1] - delta
        cur = vertices[i] - delta
        area += cur.x*prev.y - cur.y*prev.x
        edge += prev.mdist(cur)
    area = abs(area // 2)
    interior = area - edge // 2 + 1
    return edge + interior


steps = read()
print('Star 1:', dig_lagoon(dig_edge(steps)))
print('Star 2:', dig_lagoon(dig_edge_hex(steps)))