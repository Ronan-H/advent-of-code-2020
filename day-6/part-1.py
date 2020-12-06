
# I added an extra new line to the end of the input file
# so that a special condition wouldn't be needed for EOF

count_sum = 0
questions = set()

with open('./input') as input_file:
    for line in input_file:
        if line == '\n':
            count_sum += len(questions)
            questions = set()
        else:
            questions |= set(line[:-1])
    input_file.close()

print(count_sum)
