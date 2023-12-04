from aoc import *


cards = []
for line in read(sep=": "):
    cards.append([allints(x) for x in line[1].split("|")])

total = 0
copies = [1] * len(cards)
for i, card in enumerate(cards):
    wc = sum(x in card[0] for x in card[1])
    for z in range(i + 1, i + 1 + wc):
        copies[z] += copies[i]
    if wc:
        total += 2 ** (wc - 1)
print("Star 1:", total)
print("Star 2:", sum(copies))
