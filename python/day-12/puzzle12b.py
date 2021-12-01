fin = open('input.txt')
instructions = fin.read().split('\n')
del instructions[-1]
ship_pos = [0,0]
way_pos = [10,1]
facing = 1
for inst in instructions:
    action = inst[0]
    value = int(inst[1:])
    #print(action, value)
    if action == 'N':
        way_pos[1] += value
    elif action == 'S':
        way_pos[1] -= value
    elif action == 'E':
        way_pos[0] += value
    elif action == 'W':
        way_pos[0] -= value

    elif action == 'L':
        if value == 90:
            way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]
        elif value == 180:
            way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
        elif value == 270:
            way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
    elif action == 'R':
        if value == 90:
            way_pos[0], way_pos[1] = way_pos[1], -way_pos[0]
        elif value == 180:
            way_pos[0], way_pos[1] = -way_pos[0], -way_pos[1]
        elif value == 270:
            way_pos[0], way_pos[1] = -way_pos[1], way_pos[0]

    elif action == 'F':
        ship_pos[0] += way_pos[0]*value
        ship_pos[1] += way_pos[1]*value
    # print(ship_pos, way_pos)
    # print()
print(abs(ship_pos[0]) + abs(ship_pos[1]))
