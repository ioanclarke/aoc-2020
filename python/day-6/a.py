def main():
    groups = open('input.txt').read().split('\n\n')
    print(sum(get_number_of_yesses_in_group(g) for g in groups))

def get_number_of_yesses_in_group(group):
    responses = group.split('\n')
    return len(set(x for r in responses for x in get_yes_questions_in_response(r)))

def get_yes_questions_in_response(response):
    return {q for q in response}

main()