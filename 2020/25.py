from itertools import islice


def enciter(subj=7):
    val = 1
    while True:
        val *= subj
        val %= 20201227
        yield val


def findloopsize(a, b):
    size_a, size_b = None, None
    for i, val in enumerate(enciter()):
        if val == a:
            size_a = i + 1
        if val == b:
            size_b = i + 1
        if size_a is not None and size_b is not None:
            return size_a, size_b


def star1():
    card_key, door_key = 7573546, 17786549
    size_card, size_door = findloopsize(card_key, door_key)
    print(next(islice(enciter(card_key), size_door-1, None)))


print('Star 1:')
star1()