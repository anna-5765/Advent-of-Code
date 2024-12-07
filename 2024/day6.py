# Day 6 - Guard Gallivant

import networkx as nx
import itertools
import matplotlib.pyplot as plt

# Load input
with open("day6.txt", "r") as file:
    # Make the environment a 2d matrix
    env = [[char for char in line.rstrip('\n')] for line in file.readlines()]

# Find height and width of environment bounds
h, w = len(env), len(env[0])

class Position:
    def __init__(self, location, direction):
        self.location = location    # tuple of (x,y)
        self.direction = direction  # tuple like (1, 0) or (0, -1)

    def next_location(self):
        return tuple(map(sum, zip(self.location, self.direction)))
    
    def move(self):
        self.location = tuple(map(sum, zip(self.location, self.direction))) # moves in current direction

    # Find direction of right turn
    def turn_right(self):
        if self.direction == (0, 1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (-1, 0)
        else:
            self.direction = (0, 1)

# Create grid pose network
G = nx.MultiDiGraph()
for i, j in itertools.product(range(h), range(w)):
    node_name = (i,j)
    G.add_node(node_name)

# Find hash locations
hash_locations = set()
for i, line in enumerate(env):
    for j, symbol in enumerate(line):
        if symbol == '#':
            hash_locations.add((i,j))

# Find start
for i, line in enumerate(env):
    for j, symbol in enumerate(line):
        if symbol == '^':
            start = (i,j)

# Make path
current = Position(start, (-1, 0))
traveled = set()
traveled_list = [] # for visualization
while current.location in G:
    traveled.add(current.location)
    traveled_list.append(current.location)
    if current.next_location() not in hash_locations:
        current.move()
    else:
        current.turn_right()
        current.move()

# # Graph visualization
# # pos for grid makes even spaced nodes to look like a grid
# for i in range(len(traveled_list[0:-1])):
#     G.add_edge(traveled_list[i], traveled_list[i+1])
# pos = {(i,j): (j, -i) for i,j in G.nodes()}  # Note: -i to flip y-axis
# nx.draw(G, pos, node_size=100)
# plt.grid(True)
# plt.show()
   
print(len(traveled)) # part 1 answer

