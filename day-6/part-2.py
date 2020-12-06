
# I added an extra new line to the end of the input file
# so that a special condition wouldn't be needed for EOF

count = 0
qs = set()
q_lines = []

with open('./input') as input_file:
    for line in input_file:
        if line == '\n':
            count += sum(all(q in q_line for q_line in q_lines) for q in qs)
            qs = set()
            q_lines = []
        else:
            unique_qs = set(line[:-1])
            qs |= unique_qs
            q_lines.append(unique_qs)
    input_file.close()

print(count)
