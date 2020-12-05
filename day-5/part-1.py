import math


def binary_search(dirs, lower, upper):
    if lower == upper:
        # found seat
        return lower

    if dirs[0] in ['F', 'L']:
        # lower
        return binary_search(dirs[1:], lower, lower + (upper - lower) // 2)
    else:
        # upper
        return binary_search(dirs[1:], lower + math.ceil((upper - lower) / 2), upper)


highest = -1
with open('./input') as input_file:
    for line in input_file:
        dirs = line[:-1]  # excludes newline
        row = binary_search(dirs[:-3], 0, 127)
        col = binary_search(dirs[-3:], 0, 7)
        seat_id = (row * 8) + col
        highest = max(highest, seat_id)
    input_file.close()

print(highest)
