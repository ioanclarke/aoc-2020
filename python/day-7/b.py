def count_bags_in_bag(bag, bags):
    if bags[bag] == {}:
        return 0
    else:
        res = 0
        for subbag, count in bags[bag].items():
            res += int(count) + int(count) * count_bags_in_bag(subbag, bags)
            print(subbag, count)
        return res

print(count_bags_in_bag('shiny gold', bags))

def main():
    inp = open('input.txt')
    bag_contains_map = {get_bag_name(line): get_contained_bags(get_contained_bags_string(line)) for line in inp}
    print(sum(bag_contains_gold(bag, bag_contains_map) for bag in bag_contains_map))

def get_bag_name(line):
    return line[:line.find('bags') - 1]

def get_contained_bags_string(line):
    return line[line.find('contain') + 8:]

def get_contained_bags(s):
    contained_bags = []
    while has_number(s):
        new_bag = s[find_number(s) + 2 : s.find('bag') - 1]
        contained_bags.append(new_bag)
        s = s[s.find('bag') + 3:]
    
    return contained_bags

def has_number(s):
    return any(c.isdigit() for c in s)

def find_number(s):
    for pos, c in enumerate(s):
        if c.isdigit():
            return pos

def bag_contains_gold(bag, bag_contains_map):
    if bag_contains_map[bag] == []:
        return False

    if 'shiny gold' in bag_contains_map[bag]:
        return True
    
    return any(bag_contains_gold(subbag, bag_contains_map) for subbag in bag_contains_map[bag])
    
main()