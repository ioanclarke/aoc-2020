fin = open('input.txt')
numbers = fin.read().split('\n')
del numbers[-1]
for i, num in enumerate(numbers):
    numbers[i] = int(num)
numbers.sort()
gaps_1 = 0
gaps_3 = 1
if numbers[0] == 1:
    gaps_1 += 1
elif numers[0] == 3:
    gaps_3 += 1

for i in range(len(numbers) - 1):
    if numbers[i+1] - numbers[i] == 1:
        gaps_1 += 1
    elif numbers[i+1] - numbers[i] == 3:
        gaps_3 += 1

print(gaps_1*gaps_3)
