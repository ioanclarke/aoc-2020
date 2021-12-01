def is_valid(line):
    space = line.find(' ')
    dash = line.find('-')

    nums = line[:space]
    lower = int(nums[:dash]) - 1
    upper = int(nums[dash + 1:]) - 1
    letter = line[space + 1: space + 2]
    password = line[line.find(':') + 2:]

    return (password[lower] == letter) ^ (password[upper] == letter)
        
data = open('input.txt').read().split('\n')[:-1]
print(sum(is_valid(line) for line in data))
