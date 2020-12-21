import re
from itertools import chain


def parse_dish(line):
    dish, allergens = re.match('(.+?) \(contains (.+?)\)', line).groups()
    return dish.split(), allergens.split(', ')


def find_allergens(dishes):
    allergens = dict()
    tmp = dict()
    for dish_ing, dish_allerg in dishes:
        for a in dish_allerg:
            tmp.setdefault(a, set(dish_ing)).intersection_update(dish_ing)
    while tmp:
        allergen, ingredient = next((a, ing) for a, ing in tmp.items() if len(ing) == 1)
        allergens[next(iter(ingredient))] = allergen
        del tmp[allergen]
        for v in tmp.values():
            v -= ingredient
    return allergens


def star1():
    dishes = [parse_dish(line.strip()) for line in open('input.txt')]
    allergens = find_allergens(dishes)
    print(sum(1 for ingridient in chain.from_iterable(d[0] for d in dishes) if ingridient not in allergens))


def star2():
    dishes = [parse_dish(line.strip()) for line in open('input.txt')]
    allergens = find_allergens(dishes)
    print(','.join(sorted(allergens.keys(), key=allergens.get)))


print('Star 1:')
star1()
print('Star 2:')
star2()
