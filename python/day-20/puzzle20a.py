fin = open('input.txt')
data = fin.read().split('\n\n')

tiles = {}
for tile in data:
    tile_num = tile[5:tile.find(':')]
    tile_image = tile[tile.find(':') + 1:]
    tile_lines = tile_image.split('\n')
    del tile_lines[0]
    if tile_num == '2843':
        del tile_lines[-1]

    top = tile_lines[0]
    bottom = tile_lines[-1]
    left = []
    right = []
    for line in tile_lines:
        left.insert(0, line[0])
        right.append(line[-1])

    left = ''.join(left)
    right = ''.join(right)
    tiles[tile_num] = (top, right, bottom, left)

corners = []
for tile in tiles:
    # print(f'tile: {tile}\t{tiles[tile]}')
    unmatched = 0
    edges = tiles[tile]
    for edge in edges:
        edge_reverse = ''.join(list(reversed(edge)))
        # print(f'edge: {edge}\t{edge_reverse}')
        match = False
        for check_tile in tiles:
            if check_tile == tile:
                continue
            else:
                # print(f'\tchecking {check_tile}: {tiles[check_tile]}')
                if edge in tiles[check_tile] or edge_reverse in tiles[check_tile]:
                    # print(f'\tfound {edge} in {check_tile}, {tiles[check_tile]}')
                    match = True
                    break
        if not match:
            unmatched += 1
    if unmatched == 2:
        corners.append(tile)

print(corners)
res = 1
for n in corners:
    res *= int(n)
print(res)
