
input_file = open('input')
nums = [int(line) for line in input_file.readlines()]
input_file.close()

target = 1398413738
end = len(nums)

for start in range(end):
    rolling_sum, smallest, largest = 0, 0, 0
    for cur_index in range(start, end):
        cur = nums[cur_index]
        rolling_sum += nums[cur_index]

        if rolling_sum > target:
            break

        if cur_index == start:
            smallest = cur
            largest = cur
        else:
            smallest = min(smallest, cur)
            largest = max(largest, cur)

            if rolling_sum == target:
                result = smallest + largest
                print(result)
                exit(0)
