def create_inital_state(lines):
    for line in lines:
        steps = []
        while line:
            if line[0] == 'e' or line[0] == 'w':
                steps.append(line[0])
                line = line[1:]
            elif line[0] == 'n' or line[0] == 's':
                steps.append(line[:2])
                line = line[2:]
        coords = [0,0]

        for step in steps:
            parity = 'even' if coords[1] % 2 == 0 else 'odd'

            if step == 'e': coords[0] += 1

            elif step == 'w': coords[0] -= 1

            elif step == 'ne':
                coords[1] -= 1
                if parity == 'even': coords[0] += 1

            elif step == 'se':
                coords[1] += 1
                if parity == 'even': coords[0] += 1

            elif step == 'nw':
                coords[1] -= 1
                if parity == 'odd': coords[0] -= 1

            elif step == 'sw':
                coords[1] += 1
                if parity == 'odd': coords[0] -= 1

        coords = tuple(coords)
        if coords in tiles:
            tiles[coords] = 'b' if tiles[coords] == 'w' else 'w'
        else:
            tiles[coords] = 'b'


def update_tiles():
    iter_tiles = tiles.copy()
    added = {}
    for tile, col in iter_tiles.items():
        neighbour_coords = get_neighbour_coords(tile)
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
        if col == 'b' and (numOfBlack == 0 or numOfBlack > 2):
            tiles[tile] = 'w'
        elif col == 'w' and numOfBlack == 2:
            tiles[tile] = 'b'


def add_tile(tile, iter_tiles):
    neighbour_coords = get_neighbour_coords(tile)
    neighbours = []
    neighbours = [iter_tiles.get(coord, 'w') for coord in neighbour_coords]
    numOfBlack = neighbours.count('b')
    tiles[tile] = 'b' if numOfBlack == 2 else 'w'


def get_neighbour_coords(tile):
                        #East     West
    neighbour_coords = [(1, 0), (-1, 0)]
    if tile[1] % 2 == 0:
                               #   NE       SE      NW      SW
        neighbour_coords.extend([(1, -1), (1, 1), (0, -1), (0, 1)])
    elif tile[1] % 2 == 1:
                               #   NE       SE       NW        SW
        neighbour_coords.extend([(0, -1), (0, 1), (-1, -1), (-1, 1)])
    neighbour_coords = [(tile[0] + coord[0], tile[1] + coord[1]) for coord in neighbour_coords]
    return neighbour_coords


def count_tiles():
    count = sum(val == 'b' for val in tiles.values())
    return count


def print_tiles(r=10):
    columns = '    '
    for i in range(-r, r):
        columns += '{:>3}'.format(i)
    print(columns)
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


if __name__ == '__main__':
    fin = open('input.txt')
    lines = fin.read().split('\n')
    del lines[-1]
    tiles = {}
    create_inital_state(lines)
    print(f'initial. count: {count_tiles()}')
    print_tiles()

    for i in range (100):
        update_tiles()
    print(f'count: {count_tiles()}')
