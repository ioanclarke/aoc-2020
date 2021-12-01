from string import ascii_lowercase

def main():
    groups = open('input.txt').read().split('\n\n')
    print(sum(get_number_of_yesses_in_group(g) for g in groups))

def get_number_of_yesses_in_group(group):
    responses = group.split('\n')
    return len([c for c in ascii_lowercase if all(c in r for r in responses)])
    
main()
