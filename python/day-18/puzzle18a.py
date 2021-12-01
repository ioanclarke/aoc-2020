def find_inside_expr(expr):
    #print(f'find_inside_expr called on {expr}')
    level = 1
    for i, c in enumerate(expr[1:], 1):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
            if level == 0:
                #print(f'inside of {expr} is {expr[1:i]}')
                return expr[1:i]

def evaluate(expr):
    #print(f'evaluating {expr}')
    res = None
    i = 0
    while i < len(expr):
        #print(f'i is {i}')
        if expr[i] == '(':
            sub_expr = find_inside_expr(expr[i:])
            if res == None:
                res = evaluate(sub_expr)
            elif op == '+':
                #print(f'adding {evaluate(sub_expr)} to res')
                res += evaluate(sub_expr)
            elif op == '*':
                #print(f'multiplying res by {evaluate(sub_expr)}')
                res *= evaluate(sub_expr)
            i += len(sub_expr) + 2
            #print(f'res = {res}')

        elif expr[i].isdigit():
            if res == None:
                res = int(expr[i])
            elif op == '+':
                #print(f'adding {expr[i]} to res')
                res += int(expr[i])
            elif op == '*':
                #print(f'multiplying res by {expr[i]}')
                res *= int(expr[i])
            i += 1
            #print(f'res = {res}')
        else:
            op = expr[i]
            i += 1
    return res


fin = open('input.txt')
sums = fin.read().split('\n')
del sums[-1]

#print(find_inside_expr('(2+3+(4+5))+7'))
total = 0
values = []
for line in sums:
    #print(line)
    expr = ''.join(line.split(' '))
    #print(expr)
    values.append(evaluate(expr))
    total += values[-1]

#print(values)
print(total)
