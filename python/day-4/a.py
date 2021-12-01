def is_valid(passport):
    fields = [f[:f.find(':')] for f in passport.split()]
    return all(f in fields for f in required_fields)

passports = open('input.txt').read().split('\n\n')
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

print(sum(is_valid(p) for p in passports))
