
input_file = open('./input')
lines = input_file.readlines()
input_file.close()

num_valid = 0

for line in lines:
    parts = line.split()
    policy_letter = parts[1][0]
    indexes = set(int(n) - 1 for n in parts[0].split('-'))
    password = parts[2]
    num_policy_letters = sum(1 if c == policy_letter and i in indexes else 0 for i, c in enumerate(password))

    if num_policy_letters == 1:
        num_valid += 1

print('Num valid:', num_valid)
