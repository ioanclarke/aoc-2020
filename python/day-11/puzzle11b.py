def update_state(state):

    new_grid = []
    num_of_rows = len(state)
    num_of_columns = len(state[0])

    #Copies the contents of state to new_grid, with each string in
    #state split into a list of individual characters in new_grid
    for i in range(num_of_rows):
        new_grid.append(list(state[i]))

    #Iterates through each cell of the grid, finds its neighbours, and applies
    #the rules that determine what the cell should contain in the next state of
    #the state.
    for row in range(num_of_rows):
        for column in range(num_of_columns):
            num_of_X = 0
            num_of_O = 0
            neighbours = []

            #Adds the cell to the North of the current cell to the list of the
            #current cell's neighbours.
            if row != 0:
                temp_row = row - 1
                while temp_row >= 0 and state[temp_row][column] == '.':
                    temp_row -= 1
                if temp_row >= 0:
                    neighbours.append(state[temp_row][column])

            #Adds the cell to the South of the current cell to the list of the
            #current cell's neighbours.
            if row != num_of_rows - 1:
                temp_row = row + 1
                while temp_row <= num_of_rows-1 and state[temp_row][column] == '.':
                    temp_row += 1
                if temp_row <= num_of_rows-1:
                    neighbours.append(state[temp_row][column])

            #Adds the cell to the East of the current cell to the list of the
            #current cell's neighbours.
            if column != num_of_columns - 1:
                temp_column = column + 1
                while temp_column <= num_of_columns-1 and state[row][temp_column] == '.':
                    temp_column += 1
                if temp_column <= num_of_columns-1:
                    neighbours.append(state[row][temp_column])

            #Adds the cell to the West of the current cell to the list of the
            #current cell's neighbours.
            if column != 0:
                temp_column = column - 1
                while temp_column >= 0 and state[row][temp_column] == '.':
                    temp_column -= 1
                if temp_column >= 0:
                    neighbours.append(state[row][temp_column])

            #Adds the cell to the North-East of the current cell to the list of
            #the current cell's neighbours.
            if row != 0 and column != num_of_columns - 1:
                temp_row = row - 1
                temp_column = column + 1
                while temp_row >= 0 and temp_column <= num_of_columns-1 and state[temp_row][temp_column] == '.':
                    temp_row -= 1
                    temp_column += 1
                if temp_row >= 0 and temp_column <= num_of_columns-1:
                    neighbours.append(state[temp_row][temp_column])

            #Adds the cell to the South-East of the current cell to the list of
            #the current cell's neighbours.
            if row != num_of_rows - 1 and column != num_of_columns - 1:
                temp_row = row + 1
                temp_column = column + 1
                #print(state[temp_row][temp_column])
                #print(type(state), type(state[temp_row]), type(temp_row), type(temp_column), type(num_of_rows), type(num_of_columns))
                while temp_column <= num_of_columns-1 and temp_row <= num_of_rows-1 and state[temp_row][temp_column] == '.':
                    temp_row += 1
                    temp_column += 1
                if temp_row <= num_of_rows-1 and temp_column <= num_of_columns-1:
                    neighbours.append(state[temp_row][temp_column])

            #Adds the cell to the North-West of the current cell to the list of
            #the current cell's neighbours.
            if row != 0 and column != 0:
                temp_row = row - 1
                temp_column = column - 1
                while temp_row >= 0 and temp_column >= 0 and state[temp_row][temp_column] == '.':
                    temp_row -= 1
                    temp_column -= 1
                if temp_row >= 0 and temp_column >= 0:
                    neighbours.append(state[temp_row][temp_column])

            #Adds the cell to the South-West of the current cell to the list of
            #the current cell's neighbours.
            if row != num_of_rows - 1 and column != 0:
                temp_row = row + 1
                temp_column = column - 1
                while temp_row <= num_of_rows-1 and temp_column >= 0 and state[temp_row][temp_column] == '.':
                    temp_row += 1
                    temp_column -= 1
                if temp_row <= num_of_rows-1 and temp_column >= 0:
                    neighbours.append(state[temp_row][temp_column])

            #Counts the number of X cells and O cells in the current cell's neighbourhood.
            num_of_occ = neighbours.count('#')

            #Applies the first rule to the current cell if applicable.
            if state[row][column] == 'L' and num_of_occ == 0:
                new_grid[row][column] = '#'


            #Applies the second rule to the current cell if applicable.
            if state[row][column] == '#' and num_of_occ >= 5:
                new_grid[row][column] = 'L'

    #Converts the list of individual cells in each row into a string.
    for i in range(num_of_rows):
        new_grid[i] = ''.join(new_grid[i])

    return new_grid

fin = open('input.txt')
state = fin.read().split('\n')
del state[-1]

# for line in state:
#     print(line)
# print()
while True:
    old_state = state
    state = update_state(state)
    # for line in state:
    #     print(line)
    # print()
    if old_state == state:
        break

count = 0
for line in state:
    count += line.count('#')
print(count)
