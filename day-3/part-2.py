from functools import reduce

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

input_file = open('./input')
tree_map = input_file.readlines()
input_file.close()

hit_list = []

for across, down in slopes:
    x = 0
    y = 0
    hit = 0
    while y < len(tree_map):
        level = tree_map[y]
        if level[x] == '#':
            hit += 1
        x = (x + across) % (len(level) - 1)
        y += down
    hit_list.append(hit)

print(reduce(lambda a, b: a * b, hit_list))
