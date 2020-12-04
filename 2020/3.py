def read_field():
    return [line.strip() for line in open('input.txt')]


def walk(field, slope_row, slope_col):
    row, col = 0, 0
    count_trees = 0
    while row < len(field) - 1:
        row += slope_row
        col += slope_col
        col %= len(field[0])
        if field[row][col] == '#':
            count_trees += 1
    return count_trees


def star1():
    field = read_field()
    print(walk(field, 1, 3))


def star2():
    field = read_field()
    slops = [1, 3, 5, 7]
    result = 1
    for slop_col in slops:
        result *= walk(field, 1, slop_col)
    result *= walk(field, 2, 1)
    print(result)


print('Star1:')
star1()
print('Star2:')
star2()