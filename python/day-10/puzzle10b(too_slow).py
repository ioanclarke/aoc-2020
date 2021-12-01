import itertools
import time

fin = open('input.txt')
numbers = fin.read().split('\n')
del numbers[-1]
for i, num in enumerate(numbers):
    numbers[i] = int(num)
numbers.sort()
numbers.insert(0, 0)
numbers.append(numbers[-1] + 3)

count = 1
check_list = [numbers.copy()]
while check_list:
    new_check_list = []
    for li in check_list:
        for i in range(1, len(li) - 1):
            if li[i + 1] - li[i - 1] <= 3:
                removed_list = li.copy()
                del removed_list[i]
                new_check_list.append(removed_list)

    new_check_list.sort()
    check_list = list(k for k,_ in itertools.groupby(new_check_list))
    count += len(check_list)

print(count)
