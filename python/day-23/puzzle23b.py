#792845136
#389125467
input = '792845136'

node = {}
for i in range(1, len(input) - 1):
    #print(i, input[i])
    node[int(input[i])] = (int(input[i-1]), int(input[i+1]))

node[int(input[0])] = (int(input[-1]), int(input[1]))
node[int(input[-1])] = (int(input[-2]), 10)

node[10] = (int(input[-1]), 11)
node[1000000] = (999999, int(input[0]))
for i in range(len(input) + 2, 1000000):
    node[i] = (i-1, i+1)

curr = int(input[0])

for i in range(10000000):
    #print(f'current: {curr}')
    next1 = node[ curr ][1]
    next2 = node[ node [ curr ] [1] ] [1]
    next3 = node[ node [ node [ curr ] [1] ] [1] ] [1]
    curr_prev = node[curr][0]
    next3_next = node[next3][1]
    next3_next_next = node[next3_next][1]
    #print(f'pick up: {move}')

    dest = curr - 1
    if dest == 0:
        dest = 1000000
    while dest == next1 or dest == next2 or dest == next3:
        dest -= 1
        if dest == 0:
            dest = 1000000
    #print(f'destination: {dest}')

    dest_next = node[dest][1]
    dest_next_next = node[dest_next][1]
    dest_prev = node[dest][0]

    node[curr] = curr_prev, next3_next
    node[next1] = dest, next2
    node[next2] = next1, next3
    node[next3] = next2, dest_next
    node[dest_next] = next3, dest_next_next
    if curr == dest_next:
        node[curr] = next3, next3_next
    if next3_next == dest:
        node[dest] = curr, next1
    else:
        node[dest] = dest_prev, next1
        node[next3_next] = curr, next3_next_next

    #curr.prev doesn't change unless curr_prev is dest (in which case curr is dest_next)
    #curr.next always becomes next3_next

    #next3_next.prev always becomes curr
    #next3_next.next doesn't change unless next3_next is dest

    #dest.prev doesn't change
    #dest.next always becomes next1

    #dest_next.prev always becomes next3
    #dest_next.next doesn't change

    #next1.prev always becomes dest
    #next1.next always becomes next2

    #next2.prev doesn't change
    #next2.next doesn't change

    #next3.prev doesn't change
    #next3.next always becomes dest_next

    curr = node[curr][1]

print(node[1][1] * node[node[1][1]][1])
