#input = 9,12,1,4,17,0,18
#test1 = 0,3,6
#test2 = 1,3,2
#test3 = 2,1,3
#test4 = 1,2,3
l = 9,12,1,4,17,0,18
turns = {}
for i in range(1, len(l) + 1):
    turns[l[i-1]] = i

num = 0
for i in range(len(l) + 1, 2021):
    if i == 2020:
        break
    if num in turns:
        temp = num
        num = i - turns[num]
        turns[temp] = i
    else:
        turns[num] = i
        num = 0

print(num)
