fin = open('input.txt')
numbers = fin.read().split('\n')
del numbers[-1]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

preamble_length = 25
def is_sum(numbers, i):
    for j in range(preamble_length):
        if numbers[i] - numbers[i-preamble_length:i][j] in numbers[i-preamble_length:i] and numbers[i] - numbers[i-preamble_length:i][j] != numbers[i-preamble_length:i][j]:
            return True
    return False

for i in range(preamble_length,len(numbers)):
    if not is_sum(numbers, i):
        print(f'no sum for: {numbers[i]}')
        break
