from aoc.io import *
import graphlib


def simulate(inputs: dict[str, int], gates: list[tuple[str, str]]) -> int:
    ops = {b: a.split() for a, b in gates}
    graph = {b: {a1, a3} for b, [a1, _, a3] in ops.items()}
    for cur in graphlib.TopologicalSorter(graph).static_order():
        if cur not in ops:
            continue
        match ops[cur]:
            case [a, 'AND', b]: inputs[cur] = inputs[a] and inputs[b]
            case [a, 'OR', b]: inputs[cur] = inputs[a] or inputs[b]
            case [a, 'XOR', b]: inputs[cur] = inputs[a] ^ inputs[b]
    bits = [inputs[x] for x in sorted(inputs.keys(), reverse=True) if x.startswith('z')]
    return int(''.join(str(b) for b in bits), 2)


def find_gate(a, op, b) -> Optional[tuple[str, str]]:
    key = f'{a} {op} {b}'
    tmp = gate_to_output.get(key)
    if tmp is not None:
        return key, tmp
    key = f'{b} {op} {a}'
    tmp = gate_to_output.get(key)
    if tmp is not None:
        return key, tmp
    return None


def swap_wires(gates: list[tuple[str, str]], w1: str, w2: str):
    i1 = next(i for i in range(len(gates)) if gates[i][1] == w1)
    i2 = next(i for i in range(len(gates)) if gates[i][1] == w2)
    gates[i1][1] = w2
    gates[i2][1] = w1

    g1, g2 = gates[i1][0], gates[i2][0]
    gate_to_output[g1] = w2
    gate_to_output[g2] = w1
    output_to_gate[w1] = g2
    output_to_gate[w2] = g1
    


def build_adder(n: int, gates: list[tuple[str, str]], carry: str) -> tuple[str, list[str]]:
    print(f'\n\nBuilding adder #{n:02}')
    x, y = f'x{n:02}', f'y{n:02}'
    print(f'Input wires: {x}, {y}')
    zwire = f'z{n:02}'

    xor1_op = f'{x} XOR {y}'
    print(f'Looking for first XOR gate: {xor1_op} ...')
    xor1_gate, xor1_out = find_gate(x, 'XOR', y)
    print(f'Found {xor1_gate} -> {xor1_out}')

    and1_op = f'{x} AND {y}'
    print(f'Looking for first AND gate: {and1_op} ...')
    and1_gate, and1_out = find_gate(x, 'AND', y)
    print(f'Found {and1_gate} -> {and1_out}')

    wrong_wires = []
    if and1_out.startswith('z'):
        if n == 0:
            print(f'{xor1_out} and {and1_out} wires were swapped')
            swap_wires(gates, xor1_out, and1_out)
            xor1_out, and1_out = and1_out, xor1_out
            wrong_wires = [xor1_out, and1_out]
        else:
            _, out = find_gate(xor1_out, 'XOR', carry)
            print(f'{out} and {and1_out} wires were swapped')
            swap_wires(gates, out, and1_out)
            wrong_wires = [out, and1_out]
            and1_out = out
    
    if n == 0:
        return and1_out, wrong_wires
    
    xor2_op = f'{xor1_out} XOR {carry}'
    print(f'Looking for second XOR gate: {xor2_op} ...')
    tmp = find_gate(xor1_out, 'XOR', carry)
    if tmp is None:
        a, _, b = output_to_gate[zwire].split()
        true_xor1_out = a if a != carry else b
        print(f'{xor1_out} and {true_xor1_out} wires were swapped')
        swap_wires(gates, xor1_out, true_xor1_out)
        if and1_out == true_xor1_out:
            and1_out = xor1_out
        wrong_wires = [xor1_out, true_xor1_out]
        xor1_out = true_xor1_out
        tmp = find_gate(xor1_out, 'XOR', carry)
    else:
        print(f'Found {tmp[0]} -> {tmp[1]}')
    _, xor2_out = tmp
    if not xor2_out.startswith('z'):
        print(f'{xor2_out} and {zwire} wires were swapped')
        swap_wires(gates, xor2_out, zwire)
        wrong_wires = [xor2_out, zwire]
        xor2_out = zwire
    

    and2_op = f'{xor1_out} AND {carry}'
    print(f'Looking for second AND gate: {and2_op} ...')
    and2_gate, and2_out = find_gate(xor1_out, 'AND', carry)
    print(f'Found {and2_gate} -> {and2_out}')

    or_op = f'{and1_out} OR {and2_out}'
    print(f'Looking for OR gate: {or_op} ...')
    or_gate, or_out = find_gate(and1_out, 'OR', and2_out)
    print(f'Found {or_gate} -> {or_out}')
    
    return or_out, wrong_wires


def fix_circuit(inputs: dict[str, int], gates: list[tuple[str, str]]) -> list[str]:
    number_of_input_bits = sum(k.startswith('x') for k in inputs)
    wrong_wires = []
    carry = None
    for i in range(number_of_input_bits):
        carry, wires = build_adder(i, gates, carry)
        if wires:
            print(wires)
        wrong_wires.extend(wires)
    wrong_wires.sort()
    return wrong_wires


initial, gates = readblocks(sep=r': | -> ')
inputs = dict(initial)
gate_to_output = dict(gates)
output_to_gate = {b: a for a, b in gates}
print('Star 1:', simulate(inputs, gates))
print('Star 2:', ','.join(fix_circuit(inputs, gates)))


ADDER = '''\
[x00]-----+----|     ---[XOR]----[z00]
          |    |     |    |
[y00]---+-+---[XOR]--+  [ccc]
        | |          |    |
        | |          ---[AND]-----|
        | ----[AND]--------------[OR]---[ccc]
        |------|
'''