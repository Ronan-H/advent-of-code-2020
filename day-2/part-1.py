
input_file = open('./input')
lines = input_file.readlines()
input_file.close()

num_valid = 0

for line in lines:
    parts = line.split()
    policy_letter = parts[1][0]
    min_letter, max_letter = [int(n) for n in parts[0].split('-')]
    password = parts[2]
    num_policy_letters = sum(1 if c == policy_letter else 0 for c in password)

    if min_letter <= num_policy_letters <= max_letter:
        num_valid += 1

print('Num valid:', num_valid)