import time

fin = open('test1.txt')
numbers = fin.read().split('\n')
del numbers[-1]
for i, num in enumerate(numbers):
    numbers[i] = int(num)
numbers.sort()
numbers.insert(0, 0)
numbers.append(numbers[-1] + 3)

#Credit to Ce Guo for this part of the solution
res = [0] * len(numbers)
res[0] = 1

for i in range(1, len(numbers)):
    for j in range(i):
        if numbers[i] - numbers[j] <= 3:
            print(res)
            print(f'i={i},j={j}, {res[i]}+={res[j]}')

            print()
            res[i] += res[j]

print(res[-1])
