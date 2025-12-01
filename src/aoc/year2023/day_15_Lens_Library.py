from aoc.io import read


def compute_hash(s: str) -> int:
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def focusing_power(boxes: list[dict[str, int]]) -> int:
    total = 0
    for i, box in enumerate(boxes):
        for j, (_, f) in enumerate(box.items()):
            total += (i + 1) * (j + 1) * f
    return total


def star1():
    steps = read(year=2023, day=15, sep=',', parse=str)[0]
    return sum(compute_hash(s) for s in steps)


def star2():
    steps = read(year=2023, day=15, sep=',', parse=str)[0]
    boxes = [dict() for _ in range(256)]
    for step in steps:
        if step[-1] == '-':
            h = compute_hash(step[:-1])
            boxes[h].pop(step[:-1], None)
            continue
        label, focal = step.split('=')
        h = compute_hash(label)
        boxes[h][label] = int(focal)
    return focusing_power(boxes)
