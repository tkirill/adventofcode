from typing import Dict, Callable
from functools import cache


lines = [l.strip() for l in open('07_input.txt')]

MASK16 = 0xFFFF


def build_board() -> Dict[str, Callable[[], int]]:
    wires = dict()

    def build_op(source):
        if 'NOT' in source:
            input_wire = source.split()[1]
            return lambda: ~wires[input_wire]()
        elif 'LSHIFT' in source:
            input_wire, shift = source.split(' LSHIFT ')
            return lambda: (wires[input_wire]() << int(shift)) & MASK16
        elif 'RSHIFT' in source:
            input_wire, shift = source.split(' RSHIFT ')
            return lambda: wires[input_wire]() >> int(shift)
        elif '1 AND' in source:
            wire = source.split()[-1]
            return lambda: wires[wire]() & 1
        elif 'AND' in source:
            wire1, wire2 = source.split(' AND ')
            return lambda: wires[wire1]() & wires[wire2]()
        elif 'OR' in source:
            wire1, wire2 = source.split(' OR ')
            return lambda: wires[wire1]() | wires[wire2]()
        elif source.isdecimal():
            return lambda: int(source)
        else:
            return lambda: wires[source]()


    for line in open('07_input.txt'):
        source, wire = line.strip().split(' -> ')
        wires[wire] = cache(build_op(source))
    return wires


b = build_board()
tmp = b['a']()
print('Star 1:', tmp)

b = build_board()
b['b'] = lambda: tmp
print('Star 2:', b['a']())