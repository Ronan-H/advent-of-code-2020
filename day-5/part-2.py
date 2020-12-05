from math import ceil


def binary_search(dirs, lower, upper):
    if lower == upper:
        # found seat
        return lower

    if dirs[0] in ['F', 'L']:
        # lower
        return binary_search(dirs[1:], lower, lower + (upper - lower) // 2)
    else:
        # upper
        return binary_search(dirs[1:], lower + ceil((upper - lower) / 2), upper)


seat_ids = []
with open('./input') as input_file:
    for line in input_file:
        dirs = line[:-1]  # excludes newline
        row = binary_search(dirs[:-3], 0, 127)
        col = binary_search(dirs[-3:], 0, 7)
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)
    input_file.close()

seat_ids.sort()
my_seat = next(a + 1 for a, b in zip(seat_ids, seat_ids[1:]) if b - a == 2)
print(my_seat)
