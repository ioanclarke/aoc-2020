from functools import reduce
from operator import mul


def trees_hit(slope):
    count = 0
    pos = [0, 0]
    d_x, d_y = slope[1], slope[0]

    for pos[0] in range(0, len(data), d_y):
        pos[0] += d_y
        pos[1] = (pos[1] + d_x) % width

        if pos[0] <= len(data) - 1 and grid[pos[0]][pos[1]] == '#':
            count += 1

    return count


data = open('input.txt').read().split()
grid = [list(line) for line in data]
width = len(grid[0])

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
counts = [trees_hit(slope) for slope in slopes]

print(reduce(mul, counts))
