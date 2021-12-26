from utils import *
from itertools import combinations
from typing import Optional, Set
from dataclasses import dataclass


@dataclass(frozen=True)
class Cubiod:
    # NB: Not really a cubiod, but a grid-aligned rectangular prism
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int

    def count(self):
        return (
            (self.xmax - self.xmin + 1)
            * (self.ymax - self.ymin + 1)
            * (self.zmax - self.zmin + 1)
        )

    def iter_corners(self):
        for x in [self.xmin, self.xmax]:
            for y in [self.ymin, self.ymax]:
                for z in [self.zmin, self.zmax]:
                    yield (x, y, z)

    def small(self):
        return all(all(abs(p) <= 50 for p in corner) for corner in self.iter_corners())

    def intersects(self, other: "Cubiod") -> bool:
        return not (
            other.xmin > self.xmax
            or other.xmax < self.xmin
            or other.ymin > self.ymax
            or other.ymax < self.ymin
            or other.zmin > self.zmax
            or other.zmax < self.zmin
        )

    def intersection(self, other: "Cubiod") -> Optional["Cubiod"]:
        if not self.intersects(other):
            return None

        return Cubiod(
            max(self.xmin, other.xmin),
            min(self.xmax, other.xmax),
            max(self.ymin, other.ymin),
            min(self.ymax, other.ymax),
            max(self.zmin, other.zmin),
            min(self.zmax, other.zmax),
        )

    def remove(self, other: "Cubiod") -> Set["Cubiod"]:
        """
        Removes an internal segment of this cuboid by
            returning (up to) 6 mutually exclusive
            segments
        """
        new_parts = set()
        # top:
        zmin = other.zmax + 1
        if zmin <= self.zmax:
            c = Cubiod(self.xmin, self.xmax, self.ymin, self.ymax, zmin, self.zmax)
            new_parts.add(c)
            zmin -= 1
        else:
            zmin = self.zmax
        # bottom:
        zmax = other.zmin - 1
        if zmax >= self.zmin:
            c = Cubiod(self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, zmax)
            new_parts.add(c)
            zmax += 1
        else:
            zmax = self.zmin

        # right/long:
        xmin = other.xmax + 1
        if xmin <= self.xmax:
            c = Cubiod(
                xmin, self.xmax, self.ymin, self.ymax, zmax, zmin
            )  # NB: flipped Z
            new_parts.add(c)
            xmin -= 1
        else:
            xmin = self.xmax

        # left/long:
        xmax = other.xmin - 1
        if xmax >= self.xmin:
            c = Cubiod(
                self.xmin, xmax, self.ymin, self.ymax, zmax, zmin
            )  # NB: flipped Z
            new_parts.add(c)
            xmax += 1
        else:
            xmax = self.xmin

        # back

        ymin = other.ymax + 1
        if ymin <= self.ymax:
            new_parts.add(
                Cubiod(xmax, xmin, ymin, self.ymax, zmax, zmin)
            )  # NB: x, z flipped

        ymax = other.ymin - 1
        if ymax >= self.ymin:
            new_parts.add(
                Cubiod(xmax, xmin, self.ymin, ymax, zmax, zmin)
            )  # NB: x, z flipped

        # sanity check - cannot overlap with each other
        assert all(not a.intersects(b) for (a, b) in combinations(new_parts, 2))
        # cannot overlap with other
        assert all(not a.intersects(other) for a in new_parts)
        # must overlap with self
        assert all(a.intersects(self) for a in new_parts)

        return new_parts

    def remove_intersection(self, other: "Cubiod") -> Set["Cubiod"]:
        intersection = self.intersection(other)
        if intersection is None:
            return {self}
        # entirely subsumed
        if intersection == self:
            return set()
        return self.remove(intersection)


# unit tests
assert Cubiod(10, 12, 10, 12, 10, 12).count() == 27
assert len(list(Cubiod(10, 12, 9, 12, 10, 12).iter_corners())) == 8

assert Cubiod(10, 12, 10, 12, 10, 12).intersects(Cubiod(10, 12, 9, 12, 10, 12))
assert not Cubiod(10, 12, 10, 12, 10, 12).intersects(Cubiod(20, 22, 20, 22, 20, 22))
assert Cubiod(10, 12, 10, 12, 10, 12).intersects(Cubiod(12, 22, 12, 22, 12, 22))

assert (
    Cubiod(10, 12, 10, 12, 10, 12).intersection(Cubiod(12, 22, 12, 22, 12, 22)).count()
    == 1
)
assert (
    Cubiod(10, 12, 10, 12, 10, 12).intersection(Cubiod(20, 22, 20, 22, 20, 22)) is None
)

# would fail assertion internally
Cubiod(10, 20, 10, 20, 10, 20).remove(Cubiod(11, 13, 11, 13, 11, 13))


def parse_line(line):
    on = "on" in line
    line = line.split(" ")[1].strip()
    line = line.replace("..", ",")
    line = line.replace("x=", "").replace("y=", "").replace("z=", "")
    return on, Cubiod(*map(int, line.split(",")))


inputs = [parse_line(line) for line in readlines("22_input.txt")]

# algorithm:
# for new cubiod:
#    find any intersecting cubiods. for each:
#       Remove their intersections (making many new cubiods)
#    if we are turning this on, this cuboid intersection


def solve(rules):
    activated = set()
    for (activate, cube) in rules:
        new_activated = set()
        for current in activated:
            new_activated |= current.remove_intersection(cube)
        if activate:
            new_activated.add(cube)
        activated = new_activated
    return sum(cube.count() for cube in activated)


# part 1
print(solve(filter(lambda x: x[1].small(), inputs)))
# part 2
print(solve(inputs))
