import math

fin = open('input.txt')
data = fin.read().split('\n')
del data[-1]
time = int(data[0])
buses = data[1]
buses = buses.split(',')
while 'x' in buses:
    buses.remove('x')
for i, bus in enumerate(buses):
    buses[i] = int(bus)

# print(time)
# print(buses)
min = math.inf
for bus in buses:
    id = bus
    while bus < time:
        bus += id
    if bus - time < min:
        min = bus - time
        print(f'min:{min} bus:{bus} time:{time}')
        #print('new id', id)
        min_bus = id
        #print('new min_bus', min_bus)

print('min', min)
print('min_bus', min_bus)
print(min * min_bus)
