
input_file = open('./input')
nums = [int(line) for line in input_file.readlines()]
input_file.close()

target = 2020
for i, num1 in enumerate(nums):
    sub_target = 2020 - num1
    diffs = set()
    for j, num2 in enumerate(nums):
        if i == j:
            continue

        if num2 in diffs:
            product = num1 * num2 * (sub_target - num2)
            print('Product:', product)
            exit(0)

        diffs.add(sub_target - num2)
