fin = open('input.txt')
instructions = fin.read().split('\n')
acc = 0
i = 0
visited = []
while True:
    if i in visited:
        break
    instruction = instructions[i]
    visited.append(i)
    if instruction.startswith('acc'):
        acc += int(instruction[4:])
        i += 1
    elif instruction.startswith('nop'):
        i += 1
    elif instruction.startswith('jmp'):
        i += int(instruction[4:])
print(acc)
