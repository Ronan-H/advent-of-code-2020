import re


def hgt_validator(hgt):
    unit = hgt[-2:]
    num = hgt[:-2]

    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76
    else:
        return False


hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
pid_pattern = re.compile(r'^[0-9]{9}$')
eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

field_validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: hgt_validator(x),
    'hcl': lambda x: hcl_pattern.match(x),
    'ecl': lambda x: x in eye_colours,
    'pid': lambda x: pid_pattern.match(x),
}
field_keys = field_validators.keys()
valid = 0

with open('./input') as input_file:
    valid_fields = set()
    for line in input_file:
        if line == '\n':  # end of current passport fields
            if all(field in valid_fields for field in field_keys):
                valid += 1
            valid_fields = set()
        else:
            for key, value in [field.split(':') for field in line[:-1].split(' ')]:
                if key in field_keys and field_validators[key](value):
                    valid_fields.add(key)
    # I added an extra new line to the end of the input file so the 'if' branch wouldn't have to be repeated here
    input_file.close()

print(valid)
