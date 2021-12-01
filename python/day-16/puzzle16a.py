fin = open('input.txt')
data = fin.read().split('\n')
del data[-1]
fields = data[:data.index('')]
ranges = []

for field in fields:
    new_range = []
    first_range = field[field.find(':')+2 : field.find('or ')-1]
    second_range = field[field.find('or ')+3 : ]

    new_range.append((int(first_range[:first_range.find('-')]), int(first_range[first_range.find('-')+1 : ])))
    new_range.append((int(second_range[:second_range.find('-')]), int(second_range[second_range.find('-')+1 : ])))
    # print(new_range)
    # print()
    ranges.append(new_range)

tickets = data[data.index('nearby tickets:')+1 : ]

invalids = []
for ticket in tickets:
    values = ticket.split(',')
    for value in values:
        value = int(value)
        if not any(range[0][0] <= value <= range[0][1] or range[1][0] <= value <= range[1][1] for range in ranges):
            invalids.append(value)
print(sum(invalids))
