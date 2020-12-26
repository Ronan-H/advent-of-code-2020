
def has_sum(target, nums):
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            return True
        seen.add(num)
    return False


last_n = 25
input_file = open('./input')
prev_nums = [int(next(input_file)) for _ in range(last_n)]

for line in input_file:
    next_num = int(line)

    if not has_sum(next_num, prev_nums):
        print(next_num)
        break

    del prev_nums[0]
    prev_nums.append(next_num)

input_file.close()
