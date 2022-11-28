from itertools import combinations, product


WEAPONS = [
('Dagger',        8,     4,       0),
('Shortsword',   10,     5,       0),
('Warhammer',    25,     6,       0),
('Longsword',    40,     7,       0),
('Greataxe',     74,     8,       0)
]

ARMORS = [
('Fake',     0,    0,      0),
('Leather',     13,    0,      1),
('Chainmail',   31,    0,      2),
('Splintmail',  53,    0,      3),
('Bandedmail',  75,    0,      4),
('Platemail',  102,    0,      5)
]

RINGS = [
    ('Fake',    0,     0,       0),
('Damage +1',    25,     1,       0),
('Damage +2',    50,     2,       0),
('Damage +3',   100,     3,       0),
('Defense +1',   20,     0,       1),
('Defense +2',   40,     0,       2),
('Defense +3',   80,     0,       3)
]

NAME, COST, DMG, ARMOR = 0, 1, 2, 3


def read_boss():
    boss = dict()
    for line in open('21_input.txt'):
        n, x = line.strip().split(': ')
        boss[n] = int(x)
    return boss


boss = read_boss()


def simulate(weapon, armor, rings):
    health = 100
    total_dmg = weapon[DMG]
    total_armor = 0
    boss_health = boss['Hit Points']
    total_dmg += armor[DMG]
    total_armor += armor[ARMOR]
    for r in rings:
        total_dmg += r[DMG]
        total_armor += r[ARMOR]
    
    while True:
        boss_health -= max(total_dmg - boss['Armor'], 1)
        if boss_health <= 0:
            return True
        health -= max(boss['Damage'] - total_armor, 1)
        if health <= 0:
            return False


def my_combinations():
    for w, a, r in product(WEAPONS, ARMORS, product(RINGS, repeat=2)):
        if r[0] == RINGS[0] or r[0] != r[1]:
            cost = w[COST] + a[COST] + sum(rr[COST] for rr in r)
            yield cost, w, a, r


min_cost = 1000*1000*1000
for cost, w, a, r in my_combinations():
    if cost < min_cost and simulate(w, a, r):
        min_cost = cost
print('Star 1:', min_cost)

max_cost = 0
for cost, w, a, r in my_combinations():
    if cost > max_cost and not simulate(w, a, r):
        max_cost = cost
print('Star 2:', max_cost)