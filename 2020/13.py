def star1():
    lines = [line.strip() for line in open('input.txt')]
    time_from = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != 'x']

    def waitmins(bus):
        return (bus - time_from % bus) % bus

    earliest = min(buses, key=waitmins)
    print(earliest * waitmins(earliest))


def star2():
    timetable = open('input.txt').readlines()[1].split(',')
    buses = [(i % int(bus), int(bus)) for i, bus in enumerate(reversed(timetable)) if bus != 'x']

    # find such timestamp x that x == bus1[0] (mod bus1[1]) == bus2[0] (mod bus2[1])
    def solvestep(bus1, bus2):
        cur = bus1[0]
        while cur % bus2[1] != bus2[0]:
            cur += bus1[1]
        return cur, bus1[1]*bus2[1]

    cur = solvestep(buses[0], buses[1])
    for bus in buses[2:]:
        cur = solvestep(cur, bus)
    print(cur[0] - len(timetable) + 1)


print('Star 1:')
star1()
print('Star 2:')
star2()