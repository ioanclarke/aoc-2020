#I think this solution works for part 1, but it hits maximum recursion depth before finding the answer
import copy

message_list = {}

def create_rules_dict(inp_rules):
    rule_set = {}
    for r in inp_rules:
        rule_num = int(r[:r.find(':')])
        rule = r[r.find(':') + 2:]
        #print(rule)
        if rule_num == 0:
            rule = rule.split(' ')
            rule_set[0] = [tuple(rule)]
        elif '|' in rule:
            if rule_num == 106:
                rule_set[106] = [('91'), ('20')]
            else:
                rules = rule.split('|')
                for ru in rules:
                    ru = ru.strip().split(' ')
                    rule_set.setdefault(rule_num, []).append(tuple(ru))
        elif rule == '"a"' or rule == '"b"':
            rule_set[rule_num] = [rule]
        elif rule_num == 8:
            rule_set[8] = [rule]

        else:
            ru = rule.split(' ')
            rule_set.setdefault(rule_num, []).append((ru[0], ru[1]))
    return rule_set

def expand_message(message, rules):
    global message_list

    new_messages = [[]]

    #print(f'expanding {message}')
    for c in message:

        # print(f'considering {c}')
        # if c != '"a"' and c != '"b"':
        #     print(f'rules[{c}] = {rules[int(c)]}')

        if c == '"a"':
            for i in range(len(new_messages)):
                new_messages[i].append('"a"')
        elif c == '"b"':
            for i in range(len(new_messages)):
                new_messages[i].append('"b"')
        elif rules[int(c)][0] == '"a"':
            for i in range(len(new_messages)):
                new_messages[i].append('"a"')
        elif rules[int(c)][0] == '"b"':
            for i in range(len(new_messages)):
                new_messages[i].append('"b"')
        else:
            if len(rules[int(c)]) == 1:
                for i in range(len(new_messages)):
                    new_messages[i].append(rules[int(c)][0][0])
                    new_messages[i].append(rules[int(c)][0][1])
            elif len(rules[int(c)]) == 2:
                msg_copy = copy.deepcopy(new_messages)
                new_messages += msg_copy
                for i in range(int(len(new_messages)/2)):
                    new_messages[i].append(rules[int(c)][0][0])
                    new_messages[i].append(rules[int(c)][0][1])
                for i in range(int(len(new_messages)/2), len(new_messages)):
                    new_messages[i].append(rules[int(c)][1][0])
                    new_messages[i].append(rules[int(c)][1][1])
        print(new_messages)

    for message in new_messages:
        if all(c in ('"a"','"b"') for c in message):
            message = ''.join(message).replace('"', '')
            #print(f'adding {message} to list')
            #print()
            message_list[message] = ''
        else:
            #print(f'calling expand_message on {message}')
            expand_message(message, rule_set)


fin = open('input.txt')
data = fin.read().split('\n\n')
inp_rules = data[0].split('\n')
messages = data[1].split('\n')
del messages [-1]

rule_set = create_rules_dict(inp_rules)
print('rule_set dictionary created')
expand_message(rule_set[0][0], rule_set)
print(len(message_list))

count = 0
for message in messages:
    if message in message_list:
        count += 1
print(count)
