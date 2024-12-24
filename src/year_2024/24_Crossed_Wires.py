from aoc.io import *
import graphlib

initial, gates = readblocks(sep=r': | -> ')
ops = {b: a.split() for a, b in gates}
graph = {b: {a1, a3} for b, [a1, _, a3] in ops.items()}
values = {a: b for a, b in initial}
gates_to_output = {a: b for a, b in gates}


for cur in graphlib.TopologicalSorter(graph).static_order():
    if cur not in ops:
        continue
    match ops[cur]:
        case [a, 'AND', b]: values[cur] = values[a] and values[b]
        case [a, 'OR', b]: values[cur] = values[a] or values[b]
        case [a, 'XOR', b]: values[cur] = values[a] ^ values[b]
bits = [values[x] for x in sorted(values.keys()) if x.startswith('z')]
# print(bits)
bits.reverse()
print(int(''.join(str(b) for b in bits), 2))

def find_wire(i1, op, i2):
    r = gates_to_output.get(f'{i1} {op} {i2}', None)
    if r is not None:
        return r
    return gates_to_output[f'{i2} {op} {i1}']

cur_c = 'rdm'
for i in range(1, 45):
    cur_a = f'x{i:02}'
    cur_b = f'y{i:02}'

    xor1_op = f'{cur_a} XOR {cur_b}'
    xor1_out = find_wire(cur_a, 'XOR', cur_b)
    print(xor1_op, '->', xor1_out)
    and1_op = f'{cur_a} AND {cur_b}'
    and1_out = find_wire(cur_a, 'AND', cur_b)
    print(and1_op, '->', and1_out)
    xor2_op = f'{xor1_out} XOR {cur_c}'
    xor2_out = find_wire(xor1_out, 'XOR', cur_c)
    print(xor2_op, '->', xor2_out)
    and2_op = f'{cur_c} AND {xor1_out}'
    and2_out = find_wire(cur_c, 'AND', xor1_out)
    print(and2_op, '->', and2_out)
    or_op = f'{and1_out} OR {and2_out}'
    or_out = find_wire(and1_out, 'OR', and2_out)
    print(or_op, '->', or_out)
    cur_c = or_out
    print('\n\n')

a = ['fhc', 'z06', 'qhj', 'z11', 'mwh', 'ggt', 'z35', 'hqk']
a.sort()
print(','.join(a))