
import copy

def expand_grid(grid):
    n = len(grid) + 2
    n_z = len(grid[0][0]) + 2
    bigger_grid = [[[['.' for l in range(n_z)] for k in range(n_z)] for j in range(n)] for i in range(n)]
    for x in range(1, n-1):
        for y in range(1, n-1):
            for z in range(1, n_z-1):
                for w in range(1, n_z-1):
                #print(f'{(x,y,z)} is {grid[y-1][x-1]}')
                    if n == 5:
                        bigger_grid[x][y][z][w] = grid[y-1][x-1]
                    else:
                        bigger_grid[x][y][z][w] = grid[y-1][x-1][z-1][w-1]
    return bigger_grid


def update_grid(grid):
    updated_grid = copy.deepcopy(grid)
    n = len(grid)
    n_z = len(grid[0][0])
    c_to_ac = 0
    c_to_in = 0
    for x in range(n):
        for y in range(n):
            for z in range(n_z):
                for w in range(n_z):
                    neighbours = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            for k in range(-1, 2):
                                for l in range(-1, 2):
                                    if 0 <= x+i < n and 0 <= y+j < n and 0 <= z+k < n_z and 0 <= w+l < n_z and not(i==0 and j==0 and k==0 and l==0):
                                        neighbours.append(grid[x+i][y+j][z+k][w+l])


                    active = neighbours.count('#')
                    #print(f'active neighbours: {active}')
                    #print(f'{(x,y,z)} - {grid[x][y][z]} has {active} active neighbours')
                    
                    if grid[x][y][z][w] == '#':
                        if active == 2 or active == 3:
                            updated_grid[x][y][z][w] = '#'
                        else:
                            c_to_in += 1
                            #print(f'changing {(x,y,z)} from # to .')
                            updated_grid[x][y][z][w] = '.'

                    if grid[x][y][z][w] == '.':
                        if active == 3:
                            updated_grid[x][y][z][w] = '#'
                            c_to_ac += 1
                            #print(f'changing {(x,y,z)} from . to #')
                        else:
                            updated_grid[x][y][z][w] = '.'
    print(f'.\'s changed to #\'s {c_to_ac}')
    print(f'#\'s changed to .\'s {c_to_in}')
    return updated_grid


def display_active(grid):
    n = len(grid)
    n_z = len(grid[0][0])
    active = 0
    for x in range(n):
        for y in range(n):
            for z in range(n_z):
                for w in range(n_z):
                    if grid[x][y][z][w] == '#':
                        active += 1
    print(f'active: {active}')
    print()


fin = open('input.txt')
data = fin.read().split('\n')
del data[-1]
n = len(data)

for i, row in enumerate(data):
    data[i] = list(row)

grid = [[(i,j) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        grid[i][j] = data[i][j]

for i in range(6):
    grid = expand_grid(grid)
    grid = update_grid(grid)
    display_active(grid)
