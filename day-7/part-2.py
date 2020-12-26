
class Bag:
    def __init__(self, colour):
        self.colour = colour
        self.children = []

    def add_child(self, child, quantity):
        self.children.append((child, quantity))

    def num_children(self, bag_graph):
        return sum(
                   (bag_graph[child.colour].num_children(bag_graph) + 1) * quantity
                   for child, quantity in self.children
               )


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
    for bag_colour, bag_quantity in zip(colours, quantities):
        full_colour = ' '.join(bag_colour)
        inner_bag = Bag(full_colour)
        outer_bag.add_child(inner_bag, int(bag_quantity))
    bags[outer_colour] = outer_bag
input_file.close()

count = bags['shiny gold'].num_children(bags)

print(count)
