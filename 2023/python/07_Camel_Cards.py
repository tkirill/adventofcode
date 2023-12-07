from aoc import *
from collections import Counter


STRENGTH = list(
    reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
)


def score(hand):
    return list(x for _, x in Counter(hand).most_common())


def joker_score(hand):
    if "J" in hand:
        return max(score(hand.replace("J", x)) for x in STRENGTH)
    return score(hand)


def indices(items: Iterable, arr: list) -> list[int]:
    return [arr.index(x) for x in items]


hands = [(str(h), b) for h, b in read()]
hands.sort(key=lambda x: (score(x[0]), indices(x[0], STRENGTH)))
print("Star 1:", sum((i + 1) * x[1] for i, x in enumerate(hands)))

STRENGTH.pop(STRENGTH.index("J"))
STRENGTH.insert(0, "J")
hands.sort(key=lambda x: (joker_score(x[0]), indices(x[0], STRENGTH)))
print("Star 2:", sum((i + 1) * x[1] for i, x in enumerate(hands)))
