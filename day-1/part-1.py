
input_file = open('./input')
nums = [int(line) for line in input_file.readlines()]
input_file.close()

diffs = set()
target = 2020
for num in nums:
    if num in diffs:
        product = num * (target - num)
        print('Product:', product)
        break
    diffs.add(target - num)
