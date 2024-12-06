from aoc.io import *
from collections import Counter
from collections.abc import Iterable


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


###############
# Visualisation
###############


from blessed import Terminal
import time

term = Terminal()
hands = [(str(h), b) for h, b in read()]


def kind(hand):
    match score(hand):
        case [5]:
            return 0
        case [4, 1]:
            return 1
        case [3, 2]:
            return 2
        case [3, 1, 1]:
            return 3
        case [2, 2, 1]:
            return 4
        case [2, 1, 1, 1]:
            return 5
    return 6


def print_with_kind(hand, kind):
    match kind:
        case 0:
            print(term.bright_red(hand), end="")
        case 1:
            print(term.bright_magenta(hand), end="")
        case 2:
            print(term.bright_blue(hand), end="")
        case 3:
            print(term.bright_green(hand), end="")
        case 4:
            print(term.bright_yellow(hand), end="")
        case 5:
            print(term.bright_cyan(hand), end="")
        case 6:
            print(term.bright_white(hand), end="")


with term.fullscreen():
    print(term.home(), end="")
    print_with_kind("[Five of a kind]", 0)
    print_with_kind(" | [Four of a kind]", 1)
    print_with_kind(" | [Full house]", 2)
    print_with_kind(" | [Three of a kind]", 3)
    print_with_kind(" | [Two pair]", 4)
    print_with_kind(" | [One pair]", 5)
    print_with_kind(" | [High card]", 6)
    print()
    print()
    with term.location():
        for r in range(8):
            for c in range(25):
                print(hands[r * 25 + c][0], "", end="")
            print()
    time.sleep(1)
    kinds = [kind(h[0]) for h in hands]
    for cur_kind in range(7):
        for r in range(8):
            for c in range(25):
                k = kinds[r * 25 + c]
                if k == cur_kind:
                    with term.location():
                        print(term.move_xy(c * 6, r + 2), end="")
                        print_with_kind(hands[r * 25 + c][0] + " ", k)
                    time.sleep(0.025)
    term.inkey()
