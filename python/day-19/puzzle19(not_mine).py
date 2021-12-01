"""
This beautiful code does not belong to me and I take zero credit for it. Ce Guo was kind
enough to give me his code for this day so I was able to get all the golden stars.
I am including this code and file in my repo purely so the repo has a complete
set of solutions for AoC 2020. Thanks again, Ce.
"""
with open('input.txt') as f:
    content = f.read().split('\n')

lines = list([l.strip() for l in content])

# a dictionary for recording the whole rules
numberList = {}
# a dictionary for recording the rootnumbers
rootNumber = {}
# a dictionary for recording the test information
testDict = {}


def match_next(line, start, end, next):
    key = (start, end, tuple(next))
    # Make a judgment on whether the startlocation equals endlocation and nextlist is empty
    if start == end and not next:
        return True
    if start == end:
        return False
    if not next:
        return False

    ret = False
    # Recursive judgment: Whether the given length string satisfies two conditions
    # 1. line[start:i] should satisfy the rule (which is next[0])
    # 2. line[i:end] should satisfy recursive rules
    for i in range(start + 1, end + 1):
        if match(line, start, i, next[0]) and match_next(line, i, end, next[1:]):
            ret = True

    return ret


def match(line, start, end, rule):
    # create a testkey
    key = (start, end, rule)
    # if we have tested the condition, we can find it in our testdictionary
    if key in testDict:
        return testDict[key]

    ret = False
    # if the rule of the condition is one of our rootnumber, we can compare the line[start:end] with the letter
    if rule in rootNumber:
        ret = (line[start:end] == rootNumber[rule])

    # else we continue find nextnumber, until we find the rootnumber
    else:
        for next in numberList[rule]:
            if match_next(line, start, end, next):
                ret = True

    testDict[key] = ret
    return ret


def solve(part):
    result = 0
    for line in lines:
        # if the line is a condition, format this line and gain a dictionary as {number: [nextNumber]}
        if ':' in line:
            words = line.split()
            number = words[0][:-1]

            # for part2, we don't need to change any functions, just change the rules
            if number == '8' and part == 'part2':
                nextNumber = '42 | 42 8'
            elif number == '11' and part == 'part2':
                nextNumber = '42 31 | 42 11 31'
            else:
                nextNumber = ' '.join(words[1:])

            # deal with the original line
            if "\"" in nextNumber:
                rootNumber[number] = nextNumber[1:-1]
            else:
                nextNumbers = nextNumber.split(' | ')
                numberList[number] = [n.split(' ') for n in nextNumbers]

        # if the line is a result, begin to test this line
        elif line:
            testDict.clear()
            if match(line, 0, len(line), '0'):
                result += 1
    return result


print(solve('part1'))
print(solve('part2'))
