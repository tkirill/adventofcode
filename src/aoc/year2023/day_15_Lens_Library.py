from aoc.io import read


def compute_hash(s: str) -> int:
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def remove_lens(box: list[tuple[str, int]], label: str):
    p = next((i for i, (l, _) in enumerate(box) if l == label), None)
    if p is not None:
        del box[p]


def append_lens(box: list[tuple[str, int]], label: str, focal: int):
    p = next((i for i, (l, _) in enumerate(box) if l == label), None)
    if p is not None:
        box[p] = (label, focal)
        return
    box.append((label, focal))


def focusing_power(boxes: list[list[tuple[str, int]]]) -> int:
    total = 0
    for i, box in enumerate(boxes):
        for j, (_, f) in enumerate(box):
            total += (i + 1) * (j + 1) * f
    return total


def star1():
    steps = read(year=2023, day=15, sep=',', parse=str)[0]
    return sum(compute_hash(s) for s in steps)


def star2():
    steps = read(year=2023, day=15, sep=',', parse=str)[0]
    boxes = [[] for _ in range(256)]
    for step in steps:
        if step[-1] == '-':
            h = compute_hash(step[:-1])
            remove_lens(boxes[h], step[:-1])
            continue
        label, focal = step.split('=')
        h = compute_hash(label)
        append_lens(boxes[h], label, int(focal))
    return focusing_power(boxes)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
