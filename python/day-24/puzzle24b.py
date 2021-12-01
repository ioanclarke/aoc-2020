fin = open('input.txt')
lines = fin.read().split('\n')
del lines[-1]

tiles = {}

for line in lines:
    steps = []
    #print(line)
    while line:
        if line[0] == 'e' or line[0] == 'w':
            steps.append(line[0])
            line = line[1:]
        elif line[0] == 'n' or line[0] == 's':
            steps.append(line[:2])
            line = line[2:]
    #print(steps)
    coords = [0,0]
    #print(f'start: [0, 0]')
    for step in steps:
        if step == 'e':
            coords[0] += 1
        if step == 'w':
            coords[0] -= 1
        if step == 'ne':
            if coords[1] % 2 == 0:
                coords[0] += 1
            coords[1] -= 1
        if step == 'se':
            if coords[1] % 2 == 0:
                coords[0] += 1
            coords[1] += 1
        if step == 'nw':
            if coords[1] % 2 == 1:
                coords[0] -= 1
            coords[1] -= 1
        if step == 'sw':
            if coords[1] % 2 == 1:
                coords[0] -= 1
            coords[1] += 1

        #print(f'{step} => {coords}')
    coords = tuple(coords)
    if coords in tiles:
        if tiles[coords] == 'b':
            tiles[coords] = 'w'
        elif tiles[coords] == 'w':
            tiles[coords] == 'b'
    else:
        tiles[coords] = 'b'

count = sum(val == 'b' for val in tiles.values())



def print_tiles():
    r = 10
    out = '    '
    for i in range(-r, r):
        out += '{:>3}'.format(i)
    print(out)
    for i in range(-r, r):
        tiles_out = ''
        for j in range(-r, r):
            if (j,i) in tiles:
                tiles_out += f' {tiles[(j,i)]} '
            else:
                tiles_out += ' . '
        if i % 2 == 0:
            tiles_out = ' ' + tiles_out
        output = '{:>3} {}'.format(i, tiles_out)
        print(output)

def add_tile(tile, iter_tiles):
    #print(f'adding {tile}')
    neighbour_coords = [(1, 0), (-1, 0)]
    if tile[1] % 2 == 0:
        neighbour_coords.extend([(1, -1), (1, 1), (0, -1), (0, 1)])
    elif tile[1] % 2 == 1:
        neighbour_coords.extend([(0, -1), (0, 1), (-1, -1), (-1, 1)])
    neighbour_coords = [(tile[0] + coord[0], tile[1] + coord[1]) for coord in neighbour_coords]
    neighbours = []
    for coord in neighbour_coords:
        if coord in iter_tiles:
            neighbours.append(iter_tiles[coord])
    numOfBlack = neighbours.count('b')
    if numOfBlack == 2:
        tiles[tile] = 'b'
    else:
        tiles[tile] = 'w'

def count_tiles():
    count = sum(val == 'b' for val in tiles.values())
    return count

print(f'initial. count: {count_tiles()}')
print_tiles()
for i in range (100):
    #update existing tiles
    iter_tiles = tiles.copy()
    added = {}
    #print(len(iter_tiles))
    for tile, col in iter_tiles.items():
                            #east,    west
        neighbour_coords = [(1, 0), (-1, 0)]
        if tile[1] % 2 == 0:
                                  #north-east,south-east,north-west,south-west
            neighbour_coords.extend([(1, -1), (1, 1), (0, -1), (0, 1)])
        elif tile[1] % 2 == 1:
            neighbour_coords.extend([(0, -1), (0, 1), (-1, -1), (-1, 1)])
        neighbour_coords = [(tile[0] + coord[0], tile[1] + coord[1]) for coord in neighbour_coords]
        #print(f'neighbour_coords: {neighbour_coords}')
        neighbours = []
        for coord in neighbour_coords:
            if coord in iter_tiles:
                neighbours.append(iter_tiles[coord])
            else:
                if not coord in added:
                    added[coord] = ''
                    add_tile(coord, iter_tiles)
        #print(f'{tile}, color: {col}, neighbours: {neighbours}')
        numOfBlack = neighbours.count('b')
        #print(numOfBlack)
        if col == 'b' and (numOfBlack == 0 or numOfBlack > 2):
            result = 'changing to white'
            tiles[tile] = 'w'
        elif col == 'w' and numOfBlack == 2:
            result = 'changing to black'
            tiles[tile] = 'b'
        else:
            result = f'not changing'

        #print(result + '\n')
    #print(f'day{i+1}. count: {count_tiles()}')
    print_tiles()
    print()
    #

print(f'count: {count_tiles()}')

# for k,v in tiles.items():
#     print(k,v)
# for k,v in tiles.items():
#     print(k,v)
