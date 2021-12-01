"""
This is an abomination and contains many horrible, dreadful, awful lines of code.
READERS, BEWARE!
"""
import copy
def find_edges(tile_image):
    tile_lines = tile_image.split('\n')

    top = tile_lines[0]
    bottom = tile_lines[-1][::-1]
    left = []
    right = []

    for line in tile_lines:
        left.insert(0, line[0])
        right.append(line[-1])

    left = ''.join(left)
    right = ''.join(right)

    return (top, right, bottom, left)

filename = 'input.txt'
fin = open(filename)
data = fin.read().split('\n\n')
last = data[-1].split('\n')
del last[-1]
data[-1] = '\n'.join(last)

tiles = {}
tiles_edges = {}
for tile in data:
    tile_num = tile[5:tile.find(':')]
    tile_image = tile[tile.find(':') + 1:].replace('\n', '', 1)
    tiles[tile_num] = tile_image

    edges = find_edges(tiles[tile_num])
    tiles_edges[tile_num] = edges

def find_corner(tiles):
    for tile in tiles:
        #print(f'tile: {tile}\n{tiles[tile]}\n')
        unmatched = 0
        edges = tiles_edges[tile]
        #print(f'edges: {edges}')
        for edge in edges:
            edge_reverse = ''.join(list(reversed(edge)))
            #print(f'edge: {edge}\t{edge_reverse}')
            match = False
            for check_tile in tiles:
                if check_tile == tile:
                    continue
                else:
                    #print(f'\tchecking {check_tile}')
                    if edge in tiles_edges[check_tile] or edge_reverse in tiles_edges[check_tile]:
                        #print(f'found {edge} in {check_tile}')
                        match = True
                        break
            if match == False:
                unmatched += 1
        if unmatched == 2:
            return tile, rotate_corner(tile)

def rotate_corner(tile):
    #print(f'rotating {tile}\n{tiles[tile]}')
    rotated_tile = tiles[tile]
    rot = 0
    for i in range(4):
        top, _, __, left = find_edges(rotated_tile)
        top_reverse, left_reverse = ''.join(list(reversed(top))), ''.join(list(reversed(left)))
        left_and_top = (left, left_reverse), (top, top_reverse)
        if is_unmatched(left_and_top, tile):
            #print('found rotation')
            return rot
        else:
            rotated_tile = rotate_tile(rotated_tile, 1)
            rot += 1
            #print(rotated_tile)

            #print(rotated_tile)
            #rotate tile

def rotate_tile(tile_image, num):
    rotated_tile = tile_image
    for i in range(num):
        tile_as_list = rotated_tile.split('\n')
        length = len(tile_as_list[0])
        tile_as_2d_list = [list(elem) for elem in tile_as_list]
        #print('\nBefore rotation')
        #print(rotated_tile)
        # for l in tile_as_2d_list:
        #     print(l)
        rotated_tuple = zip(*tile_as_2d_list[::-1])
        rotated_tile_as_2d_list = [list(elem) for elem in rotated_tuple]
        #print(list(rotated_tile))
        #print('\nAfter rotation:')
        # for l in rotated_tile_as_2d_list:
        #     print(l)
        #print(rotated_tile_as_2d_list)
        rotated_tile_as_list = []
        for i in range(length):
            as_str = ''.join(rotated_tile_as_2d_list[i])
            rotated_tile_as_list.append(as_str)
        rotated_tile = '\n'.join(rotated_tile_as_list)
    return rotated_tile

def is_unmatched(edges, tile):
    for i in range(len(edges)):
        #print(f'checking {edges[i][0]} and {edges[i][1]}')
        for check_tile in tiles_edges:
            if check_tile == tile:
                continue
            else:
                #print(f'\tchecking {check_tile}')
                if edges[i][0] in tiles_edges[check_tile] or edges[i][1] in tiles_edges[check_tile]:
                    #print(f'{edges[i][0]} or {edges[i][1]} found in {tiles_edges[check_tile]}')
                    return False
    return True

def find_orientation_right(right, tile):
    #print(f'finding orientation for {tile} to fit right')
    tile_image = tiles[tile]
    left = find_edges(tile_image)[3]
    left_reversed = ''.join(list(reversed(left)))
    flipped = False
    rotations = 0
    for i in range(4):
        if left_reversed == right:
            return flipped, rotations
        else:
            tile_image = rotate_tile(tile_image, 1)
            rotations += 1
            left = find_edges(tile_image)[3]
            left_reversed = ''.join(list(reversed(left)))
    tile_image = flip_image(tile_image)
    flipped = True
    rotations = 0
    left = find_edges(tile_image)[3]
    left_reversed = ''.join(list(reversed(left)))
    for i in range(4):
        if left_reversed == right:
            #print(f'orientation: {flipped}, {rotations}')
            return flipped, rotations
        else:
            tile_image = rotate_tile(tile_image, 1)
            rotations += 1
            left = find_edges(tile_image)[3]
            left_reversed = ''.join(list(reversed(left)))
    return 'Not found'

def find_orientation_bottom(bottom, tile):
    #print(f'finding orientation for {tile} to fit bottom')
    tile_image = tiles[tile]
    top = find_edges(tile_image)[0]
    top_reversed = ''.join(list(reversed(top)))
    flipped = False
    rotations = 0
    for i in range(4):
        if top_reversed == bottom:
            return flipped, rotations
        else:
            tile_image = rotate_tile(tile_image, 1)
            rotations += 1
            top = find_edges(tile_image)[0]
            top_reversed = ''.join(list(reversed(top)))
    tile_image = flip_image(tile_image)
    flipped = True
    rotations = 0
    top = find_edges(tile_image)[0]
    top_reversed = ''.join(list(reversed(top)))
    for i in range(4):
        if top_reversed == bottom:
            return flipped, rotations
        else:
            tile_image = rotate_tile(tile_image, 1)
            rotations += 1
            top = find_edges(tile_image)[0]
            top_reversed = ''.join(list(reversed(top)))
    return 'Not found'

def find_adjacent(current_tile, side):
    #print(f'\nfinding tile to the {side} of {current_tile[0]}')
    #find which tile goes next, then find if it needs to be flipped or rotated to fit
    current_tile_name, current_tile_flipped, current_tile_rotations = current_tile
    current_tile_image = tiles[current_tile_name]

    if current_tile_flipped:
        current_tile_image = flip_image(current_tile_image)

    current_tile_image = rotate_tile(current_tile_image, current_tile_rotations)
    if side == 'right':
        match = find_edges(current_tile_image)[1]
    elif side == 'bottom':
        match = find_edges(current_tile_image)[2]

    match_reversed = ''.join(list(reversed(match)))
    for tile in tiles:
        #print(tile)
        if tile == current_tile_name:
            continue
        edges = tiles_edges[tile]
        #print(f'looking for {match} in {edges}')
        if match in edges or match_reversed in edges:
            if side == 'right':
                flipped, rotations = find_orientation_right(match, tile)
            elif side == 'bottom':
                flipped, rotations = find_orientation_bottom(match, tile)
            return tile, flipped, rotations

def flip_image(tile_image):
    tile_as_list = tile_image.split('\n')
    #print(tile_as_list)
    flipped_tile_as_list = []
    for i in range(len(tile_as_list)):
        reverse = ''.join(list(reversed(tile_as_list[i])))
        flipped_tile_as_list.append(reverse)
    flipped_tile = '\n'.join(flipped_tile_as_list)
    return flipped_tile


def create_image(image):
    length = len(image)
    display = [[[(i,j,k) for k in range(10)] for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            name, flipped, rotations = image[i][j]
            tile_image = tiles[name]
            if flipped:
                tile_image = flip_image(tile_image)
            tile_image = rotate_tile(tile_image, rotations)

            tile_lines = tile_image.split('\n')
            for k in range(10):
                display[i][j][k] = tile_lines[k]

    output = []
    for i in range(length):
        for k in range(1,9):
            str_out = []
            for j in range(length):
                str_out.append(display[i][j][k][1:-1])
            output.append(''.join(str_out))
        #output.append('')
    return output

    # output = []
    # for i in range(length):
    #     for k in range(10):
    #         str_out = []
    #         for j in range(length):
    #             str_out.append(display[i][j][k])
    #         output.append('   '.join(str_out))
    #     output.append('')
    # return '\n'.join(output)

def how_many_monsters(image):
    image = copy.copy(image)
    for i, line in enumerate(image):
        image[i] = list(line)
    #print(image)
    # print(len(image))
    # print(len(image[0]))
    print('finding monsters')
    monsters_pos = []
    count = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if i + 2 < len(image) and j + 19 < len(image[0]):
                #print(f'checking {i,j}')
                check_these = [image[i][j+18], image[i+1][j], image[i+1][j+5], image[i+1][j+6], image[i+1][j+11], image[i+1][j+12], image[i+1][j+17], image[i+1][j+18], image[i+1][j+19], image[i+2][j+1], image[i+2][j+4], image[i+2][j+7], image[i+2][j+10], image[i+2][j+13], image[i+2][j+16]]
                if all(p == '#' for p in check_these):
                    monsters_pos.append((i,j))
                    count += 1

    for pos in monsters_pos[1:]:
        i = pos[0]
        j = pos[1]
        print(i,j)
        image[i][j] = '?'
        image[i][j+18] = '1'
        image[i+1][j] = '2'
        image[i+1][j+5] = '3'
        image[i+1][j+6] = '4'
        image[i+1][j+11] = '5'
        image[i+1][j+12] = '6'
        image[i+1][j+17] = '7'
        image[i+1][j+18] = '8'
        image[i+1][j+19] = '9'
        image[i+2][j+1] = 'A'
        image[i+2][j+4] = 'B'
        image[i+2][j+7] = 'C'
        image[i+2][j+10] = 'D'
        image[i+2][j+13] = 'E'
        image[i+2][j+16] = 'F'
        image[18][17] = 'X'
    image = [''.join(x) for x in image]
    for l in image:
        print(l)
    return count


def count_waves(image):
    #print(image)
    rotations = 0
    for i in range(4):
        num_of_mon = how_many_monsters(image)
        print(f'numbers of monsters: {num_of_mon}')
        if num_of_mon == 0:
            image_newline = '\n'.join(image)
            image_newline = rotate_tile(image_newline, 1)
            image = image_newline.split('\n')
        else:
            #print(image)
            #print('\n'.join(image))
            image_str = ''.join(image)
            num_of_hash = image_str.count('#')
            return num_of_hash - num_of_mon * 15
    image_newline = '\n'.join(image)
    image_newline = flip_image(image_newline)
    image = image_newline.split('\n')
    for i in range(4):
        num_of_mon = how_many_monsters(image)
        print(f'numbers of monsters: {num_of_mon}')
        if num_of_mon == 0:
            image_newline = '\n'.join(image)
            image_newline = rotate_tile(image_newline, 1)
            image = image_newline.split('\n')
        else:

            image_str = ''.join(image)
            return image_str.count('#') - num_of_mon * 15

if filename == 'test.txt':
    length = 3
elif filename == 'input.txt':
    length = 12

image = [[(i,j) for j in range(length)] for i in range(length)]
corner, rotations = find_corner(tiles)
image[0][0] = (corner, False, rotations)
#print(image)
for i in range(length):
    for j in range(length):
        #print(i,j)
        if i == 0 and j == 0:
            continue
        elif i > 0 and j == 0:
            #print(image[0][j-1])
            image[i][j] = find_adjacent(image[i-1][0], 'bottom')
        else:
            image[i][j] = find_adjacent(image[i][j-1], 'right')

image = create_image(image)

print(f'num of waves: {count_waves(image)}')
