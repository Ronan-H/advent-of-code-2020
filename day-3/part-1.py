
x = 0
y = 0
hit = 0

with open('./input') as tree_map:
    for level in tree_map:
        if level[x] == '#':
            hit += 1
        x = (x + 3) % (len(level) - 1)
        y += 1

print(hit)
