from aoc.io import *
from dataclasses import dataclass
import more_itertools as mtls
import functools as ftls


@dataclass
class HASHable:
    val: str

    def __hash__(self):
        return ftls.reduce(lambda h, c: ((h + ord(c)) * 17) % 256, self.val, 0)


steps = read(sep=",")[0]
print("Star 1:", sum(hash(HASHable(s)) for s in steps))


steps = parselines(steps, sep="[=\-]", skip_empty=False)
boxes = {}
for label, focal in steps:
    label = HASHable(label)
    if focal == "":
        boxes.pop(label, None)
    else:
        boxes[label] = focal

total = 0
buckets = mtls.bucket(boxes.items(), key=lambda x: hash(x[0]))
for h in buckets:
    total += sum((h + 1) * (i + 1) * lens[1] for i, lens in enumerate(buckets[h]))
print("Star 2:", total)
