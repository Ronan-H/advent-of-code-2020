
valid = 0
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('./input') as input_file:
    seen_fields = set()
    for line in input_file:
        if line == '\n':
            if all(field in seen_fields for field in req_fields):
                valid += 1
            seen_fields = set()
        else:
            for field in [field.split(':')[0] for field in line.split(' ')]:
                seen_fields.add(field)
    input_file.close()
print(valid)
