fin = open('input.txt')
instructions = fin.read().split('\n')
del instructions[-1]
mem = {}
for line in instructions:
    if line.startswith('mask'):
        mask = line[line.find('=')+2:]
    elif line.startswith('mem'):
        addr = int(line[line.find('[')+1:line.find(']')])
        value = int(line[line.find('=')+1:])
        for i, char in enumerate(mask):
            if char == '1':
                addr = addr | 2**(35-i)

        addr_list = set([addr])
        for i, char in enumerate(mask):
            if char == 'X':
                new_addrs = []
                for addr in addr_list:
                    new_addrs.append(addr & (2**36-1 - 2**(35-i))) #masks 0 bit
                    new_addrs.append(addr | (2**(35-i))) #masks 1 bit
                addr_list.update(new_addrs)
        for addr in addr_list:
            mem[addr] = value

sum = 0
for v in mem.values():
    sum += v
print(sum)
