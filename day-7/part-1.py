
class Bag:
    def __init__(self, colour):
        self.colour = colour
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def contains_bag(self, colour, bag_graph, bag_cache):
        found = False
        for child in self.children:
            if child.colour == colour or bags[child.colour].contains_bag(colour, bag_graph, bag_cache):
                found = True
                break
        bag_cache[self.colour] = found
        return found


bags = {}
input_file = open('input')
for line in input_file:
    parts = line.split(' ')
    outer_colour = ' '.join(parts[:2])
    if line.endswith('no other bags.\n'):
        bags[outer_colour] = Bag(None)
        continue
    outer_bag = Bag(outer_colour)
    inner_parts = parts[4:]
    quantities = parts[4::4]
    colours = zip(parts[5::4], parts[6::4])
    for bag_colour, quantity in zip(colours, quantities):
        full_colour = ' '.join(bag_colour)
        inner_bag = Bag(full_colour)
        outer_bag.add_child(inner_bag)
    bags[outer_colour] = outer_bag
input_file.close()

count = 0

cache = dict()
target_colour = 'shiny gold'
for bag in bags:
    if cache.get(bag) or bags[bag].contains_bag(target_colour, bags, cache):
        count += 1

print(count)
