
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
