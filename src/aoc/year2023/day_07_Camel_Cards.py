from collections import Counter

from aoc.io import read


STRENGTH = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
JOKER_STRENGTH = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def combination_score(hand: str) -> list[int]:
    return [c for _, c in Counter(hand).most_common()]


def strength_score(hand: str, strength: list[str]=STRENGTH) -> list[int]:
    return [strength.index(c) for c in hand]


def joker_hand_score(hand: str) -> tuple[list[int], list[int]]:
    if 'J' not in hand:
        return combination_score(hand), strength_score(hand, JOKER_STRENGTH)
    return max(combination_score(hand.replace('J', x)) for x in hand), strength_score(hand, JOKER_STRENGTH)


def star1():
    hands = read(2023, 7, parse=str)
    hands.sort(key=lambda h: (combination_score(h[0]), strength_score(h[0])))
    return sum((i+1) * int(hand[1]) for i, hand in enumerate(hands))


def star2():
    hands = read(2023, 7, parse=str)
    hands.sort(key=lambda h: joker_hand_score(h[0]))
    return sum((i+1) * int(hand[1]) for i, hand in enumerate(hands))
