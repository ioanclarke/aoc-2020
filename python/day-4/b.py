from string import digits

def is_valid(passport):
    funcs = [
        has_required_fields,
        valid_byr, 
        valid_iyr, 
        valid_eyr, 
        valid_hgt, 
        valid_hcl, 
        valid_ecl, 
        valid_pid
    ]

    fields = {
        f.split(':')[0]:
        f.split(':')[1]
        for f in passport.split()
    }

    return all(f(fields) for f in funcs)

def has_required_fields(fields):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(f in fields for f in required_fields)

def valid_byr(fields):
    byr = int(fields['byr'])
    return 1920 <= byr <= 2002

def valid_iyr(fields):
    iyr = int(fields['iyr'])
    return 2010 <= iyr <= 2020

def valid_eyr(fields):
    eyr = int(fields['eyr'])
    return 2020 <= eyr <= 2030

def valid_hgt(fields):
    hgt = fields['hgt']
    return ((hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193) 
            or (hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76))

def valid_hcl(fields):
    hex_chars = '0123456789abcdef'
    hcl = fields['hcl']
    return hcl[0] == '#' and all(s in hex_chars for s in hcl[1:])

def valid_ecl(fields):
    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return fields['ecl'] in valid_eye_colours

def valid_pid(fields):
    pid = fields['pid']
    return len(pid) == 9 and all(s in digits for s in pid)


passports = open('input.txt').read().split('\n\n')

print(sum(is_valid(p) for p in passports))
