import re
from math import prod


def parse_ticket(line):
    return [int(x) for x in line.split(',')]


def parse_field(line):
    name, l1, r1, l2, r2 = re.match("(.+?): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
    return name, (int(l1), int(r1)), (int(l2), int(r2))


def read_input():
    fields = []
    ticket = []
    buf = []
    for line in open('input.txt'):
        if 'your ticket' in line:
            fields = [parse_field(x) for x in buf]
            buf = []
            continue
        elif 'nearby tickets' in line:
            ticket = parse_ticket(buf[-1])
            buf = []
            continue
        elif line.strip():
            buf.append(line)
    nearby = [parse_ticket(x) for x in buf]
    return fields, ticket, nearby


def is_valid_field(field, value):
    return any(r[0] <= value <= r[1] for r in field[1:])


def invalid_fields(ticket, fields):
    for x in ticket:
        if not any(is_valid_field(field, x) for field in fields):
            yield x


def star1():
    fields, ticket, nearby = read_input()
    print(sum(sum(invalid_fields(t, fields)) for t in nearby))


def is_valid_ticket(ticket, fields):
    return next(invalid_fields(ticket, fields), None) is None


def possible_positions_in_ticket(ticket, field):
    for pos, value in enumerate(ticket):
        if is_valid_field(field, value):
            yield pos


def possible_positions(field, tickets):
    result = set(possible_positions_in_ticket(tickets[0], field))
    for ticket in tickets[1:]:
        result &= set(possible_positions_in_ticket(ticket, field))
    return result


def star2():
    fields, ticket, nearby = read_input()
    valid_tickets = [t for t in nearby if is_valid_ticket(t, fields)] + [ticket]

    positions = {field[0]: possible_positions(field, valid_tickets) for field in fields}
    exact_positions = set(next(iter(pos)) for pos in positions.values() if len(pos) == 1)
    while len(exact_positions) != len(positions):
        for pos in positions.values():
            if len(pos) > 1:
                pos -= exact_positions
            if len(pos) == 1:
                exact_positions |= pos
    for k in positions:
        positions[k] = next(iter(positions[k]))

    print(prod(ticket[positions[field[0]]] for field in fields if field[0].startswith('departure')))

print('Star 1:')
star1()
print('Star 2:')
star2()