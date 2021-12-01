fin = open('input.txt')
data = fin.read().split('\n')
del data[-1]
fields = data[:data.index('')]
fields_dict = {}

for field in fields:
    field_name = field[:field.find(':')]
    new_range = []
    first_range = field[field.find(':')+2 : field.find('or ')-1]
    second_range = field[field.find('or ')+3 : ]

    new_range.append((int(first_range[:first_range.find('-')]), int(first_range[first_range.find('-')+1 : ])))
    new_range.append((int(second_range[:second_range.find('-')]), int(second_range[second_range.find('-')+1 : ])))
    fields_dict[field_name] = new_range

tickets = data[data.index('nearby tickets:')+1 : ]
valids = tickets.copy()

for ticket in tickets:
    values = ticket.split(',')
    for value in values:
        value = int(value)
        if not any(range[0][0] <= value <= range[0][1] or range[1][0] <= value <= range[1][1] for range in fields_dict.values()):
            valids.remove(ticket)

fields_pos = {}
for ticket in valids:
    values = ticket.split(',')
    for pos, v in enumerate(values):
        poss_fields = set()
        v = int(v)
        for field, ranges in fields_dict.items():
            if ranges[0][0] <= v <= ranges[0][1] or ranges[1][0] <= v <= ranges[1][1]:
                poss_fields.add(field)
        fields_pos[pos] = fields_pos.get(pos, poss_fields).intersection(poss_fields)

answers = {}
for i in range(len(fields_pos)):
    for k,v in fields_pos.items():
        if not k in answers and len(v) == 1:
            val, = v
            definite = (k, val)
            answers[k] = val

    for k,v in fields_pos.items():
        if not k in answers and definite[1] in v:
            fields_pos[k].remove(definite[1])

dep_pos = []
for k,v in answers.items():
    if v.startswith('departure'):
        dep_pos.append(k)

my_tick = data[data.index('your ticket:')+1]
my_tick = my_tick.split(',')
res = 1
for pos in dep_pos:
    res *= int(my_tick[pos])

print(res)
