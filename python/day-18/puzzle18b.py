def find_start_of_expression(expr):
    #print(f'finding start point of {expr}')
    level = 1
    for i, c in enumerate(reversed(expr[:-1])):
        if c == ')':
            level += 1
        elif c == '(':
            level -= 1
            if level == 0:
                #print(f'inside of {expr} is {expr[1:i]}')
                return i + 2
#
def find_end_of_expression(expr):
    #print(f'finding end of {expr}')
    level = 1
    for i, c in enumerate(expr[1:], 1):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
            if level == 0:
                #print(f'inside of {expr} is {expr[1:i]}')
                return i + 1
#
# def add_brackets(expr):
#     #wherever + appears in the expression, add brackets around the sub-expressions that are being added
#     i = 0
#     new_expr = list(expr)
#     #print(new_expr)
#     while i < len(expr):
#         #print(i)
#         if new_expr[i] == '+':
#             if new_expr[i-1] != ')':
#                 #print(f'adding ( before {expr[i-1]}')
#                 new_expr.insert(i-1, '(')
#             else:
#                 pos = find_start_of_expression(expr[:i])
#                 #print(new_expr[i-pos-1])
#                 new_expr.insert(i-pos, '(')
#
#             if new_expr[i+2] != '(':
#                 #print(f'adding ) after {expr[i+1]}')
#                 new_expr.insert(i+2, ')')
#
#             else:
#                 i += find_end_of_expression(expr[i+1:])
#                 #i += pos
#                 #print(f'adding ) after {expr[i]}{expr[i+1]}')
#                 new_expr.insert(i+2, ')')
#                 #print(pos)
#             #print(new_expr)
#         i += 1
#     return ''.join(new_expr)

#1 + (2 * 3) + (4 * (5 + 6))   (1 + (2 * 3)) + (4 * (5 + 6))
#                              ((1 + (2 * 3)) + (4 * (5 + 6)))
#                              ((1 + (2 * 3)) + (4 * ((5 + 6))))

#2 * 3 + (4 * 5)               2 * (3 + (4 * 5))
def add_brackets(expr):
    new_expr = list(expr)
    #print(new_expr)
    num_of_plus = new_expr.count('+')
    #print(num_of_plus)
    for i in range(num_of_plus):
        expr = ''.join(new_expr)
        pos = expr.replace('+', 'X', i).find('+')
        #print(i,pos)
        if new_expr[pos-1] != ')':
            new_expr.insert(pos-1, '(')
        else:
            start_pos = find_start_of_expression(expr[:pos])
            #print(f'pos: {pos} start_pos: {start_pos}')
            new_expr.insert(pos - start_pos, '(')

        expr = ''.join(new_expr)
        pos = expr.replace('+', 'X', i).find('+')
        if new_expr[pos+1] != '(':
            new_expr.insert(pos+2, ')')
        else:
            end_pos = find_end_of_expression(expr[pos+1:])
            #print(f'pos: {pos} end_pos: {end_pos}')
            new_expr.insert(pos + end_pos + 1, ')')
        #print(new_expr)
    return ''.join(new_expr)

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
brackets = []
for line in sums:
    #print(line)
    expr = ''.join(line.split(' '))
    #print(expr)
    expr = add_brackets(expr)
    brackets.append(expr)
    values.append(evaluate(expr))
    total += values[-1]

# for b in brackets:
#     print(b)
print(values)
print(total)
