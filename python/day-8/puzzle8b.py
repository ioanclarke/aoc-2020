fin = open('input.txt')
instructions = fin.read().split('\n')
print(instructions)

changes = []
for i, instruction in enumerate(instructions):
    if instruction.startswith('nop') or instruction.startswith('jmp'):
        changes.append(i)
print(changes)

finished = False

for change in changes:
    acc = 0
    i = 0
    visited = []
    while True:
        if i in visited:
            #print(f'changing instruction[{change}] does not work')
            break

        instruction = instructions[i]
        visited.append(i)

        if instruction == '':
            print('terminated')
            finished = True
            break

        if instruction.startswith('acc'):
            acc += int(instruction[4:])
            i += 1
        elif instruction.startswith('nop'):
            if i == change:
                i += int(instruction[4:])
            else:
                i += 1
        elif instruction.startswith('jmp'):
            if i == change:
                i += 1
            else:
                i += int(instruction[4:])
    if finished == True:
        break
print(acc)
