
input_file = open('./input')
instructions = []
for line in input_file:
    instruction = line[:-1].split(' ')
    instruction[1] = int(instruction[1])
    instructions.append(instruction)
input_file.close()

ins_no = 0
acc = 0
seen = set()

while True:
    if ins_no in seen:
        print(acc)
        break
    seen.add(ins_no)

    op, num = instructions[ins_no]
    jump = 1
    if op == 'acc':
        acc += num
    if op == 'jmp':
        jump = num
    ins_no += jump
