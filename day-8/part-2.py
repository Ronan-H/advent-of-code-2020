
input_file = open('./input')
instructions = []
for line in input_file:
    instruction = line[:-1].split(' ')
    instruction[1] = int(instruction[1])
    instructions.append(instruction)
input_file.close()


def terminates(instructions):
    ins_no = 0
    acc = 0
    seen = set()

    while True:
        if ins_no in seen:
            return False
        seen.add(ins_no)

        if ins_no >= len(instructions):
            return acc

        op, num = instructions[ins_no]
        jump = 1
        if op == 'acc':
            acc += num
        if op == 'jmp':
            jump = num
        ins_no += jump


swap = {
    'nop': 'jmp',
    'jmp': 'nop',
}

for ins in instructions:
    op, num = ins
    old = op
    if old in swap.keys():
        ins[0] = swap[old]
        result = terminates(instructions)
        ins[0] = old

        if result is not False:
            print(result)
            break
