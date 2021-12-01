data = open('input.txt').read().split()
grid = [list(line) for line in data]
width = len(grid[0])

count = 0
pos = [0, 0]
for pos[0] in range(1, len(grid)):
    pos[1] = (pos[1] + 3) % width

    if grid[pos[0]][pos[1]] == '#':
        count += 1
        
print(count)
