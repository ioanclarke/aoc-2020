#792845136
#389125467
input = '389125467  '
cups =  list(int(x) for x in input)
#print(cups)
curr = cups[0]

for i in range(100):
    print(f'move {i+1}')
    print(cups)
    print(f'current: {curr}')
    curr_pos = cups.index(curr)
    move = (cups[(curr_pos + 1) % len(cups)], cups[(curr_pos + 2 ) % len(cups)], cups[(curr_pos + 3 ) % len(cups)])
    print(f'pick up: {move[0]} {move[1]} {move[2]}')
    cups.remove(move[0])
    cups.remove(move[1])
    cups.remove(move[2])
    print(f'after picking up: {cups}')

    dest = curr - 1
    while not dest in cups:
        dest -= 1
        if dest < min(cups):
            dest = max(cups)
    print(f'destination: {dest}')

    dest_pos = cups.index(dest)
    #print(f'dest pos: {dest_pos+1}')
    cups.insert(dest_pos + 1, move[2])
    cups.insert(dest_pos + 1, move[1])
    cups.insert(dest_pos + 1, move[0])
    curr_pos = cups.index(curr)
    curr = cups[(curr_pos + 1) % len(cups)]
    print()
print(cups)
print()
pos_1 = cups.index(1)
output = []
for i in range(1, len(cups)):
    #print(cups[pos_1 + i])
    output.append(cups[(pos_1 + i) % len(cups)])
print(''.join([str(x) for x in output]))
#print(''.join(output))
