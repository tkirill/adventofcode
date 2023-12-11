from aoc import *
import itertools as itls
import more_itertools as mitls


def find_galaxies(coeff: int) -> Iterable[Vec2]:
    galaxies = [pos for pos, v in map.cellsv() if v == '#']
    empty_cols = [i for i, s in enumerate(map.columnsv()) if all(v == '.' for _, v in s)]
    empty_rows = [i for i, s in enumerate(map.rowsv()) if all(v == '.' for _, v in s)]
    
    shifted = []
    for g in galaxies:
        delta = Vec2(mitls.quantify(empty_cols, lambda c: c < g.x), mitls.quantify(empty_rows, lambda r: r < g.y))
        shifted.append(g + (coeff-1) * delta)
    return shifted


def distances(galaxies):
    return sum(a.mdist(b) for a, b in itls.combinations(galaxies))



map = Field(read(parse=list))
print('Star 1:', sum(a.mdist(b) for a, b in itls.combinations(find_galaxies(2), 2)))
print('Star 2:', sum(a.mdist(b) for a, b in itls.combinations(find_galaxies(1_000_000), 2)))