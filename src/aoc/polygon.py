import dataclasses

import aoc.grid
import aoc.vec2
import aoc.rectangle
import aoc.interval


@dataclasses.dataclass
class Polygon:

    vertices: list[aoc.vec2.Vec2]

    def edges(self):
        for i in range(1, len(self.vertices)+1):
            yield aoc.grid.GridInterval(self.vertices[i-1], self.vertices[i % len(self.vertices)])


def point_inside(poly: Polygon, point: aoc.vec2.Vec2) -> bool:
    is_inside = False
    for e in poly.edges():
        if point in e:
            return True
        if e.is_vertical:
            continue
        if e.begin.y >= point.y:
            continue
        tmp = aoc.vec2.Vec2(point.x, e.begin.y)
        if tmp in e and tmp != e.begin:
            is_inside = not is_inside
    return is_inside


def rectangle_inside(poly: Polygon, r: aoc.rectangle.Rectangle) -> bool:
    for e in poly.edges():
        if e.is_vertical:
            if not r.xmin < e.begin.x < r.xmax:
                continue
            if aoc.interval.Interval(r.ymin+1, r.ymax-1) & aoc.interval.Interval(e.begin.y, e.end.y):
                return False
        if e.is_horizontal:
            if not r.ymin < e.begin.y < r.ymax:
                continue
            if aoc.interval.Interval(r.xmin+1, r.xmax-1) & aoc.interval.Interval(e.begin.x, e.end.x):
                return False
    return (point_inside(poly, r.top_left)
            and point_inside(poly, r.top_right)
            and point_inside(poly, r.bottom_left)
            and point_inside(poly, r.bottom_right)
            and point_inside(poly, r.mid))