def get_row(bp):
    rows = list(range(128))
    for c in bp[:-3]:
        middle = len(rows) // 2
        rows = rows[:middle] if c == 'F' else rows[middle:]
    return rows[0]

def get_column(bp):
    columns = list(range(8))
    for c in bp[-3:]:
        middle = len(columns) // 2
        columns = columns[middle:] if c == 'R' else columns[:middle]
    return columns[0]

data = open('input.txt').read().split()
print(max(get_row(bp) * 8 + get_column(bp) for bp in data))
