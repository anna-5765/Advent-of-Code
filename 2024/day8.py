# Day 8 - Resonant Collinearity

from itertools import combinations

# Load input
with open("day8.txt", "r") as file:
    # Make the environment a 2d matrix
    env = [[char for char in line.rstrip("\n")] for line in file.readlines()]

# Find the environment bounds
h, w = len(env), len(env[0])

# Search for unique antennas in environment
unique_antennas = set()
for line in env:
    for sym in line:
        if sym != '.':
            unique_antennas.add(sym)

# Create a dictionary of all antennas and their locations
locations = {}
for sym in unique_antennas:
    locations[sym] = []
    positions = []

    for i in range(h):
        for j in range(w):
            if env[i][j] == sym:
                positions.append((i,j))
    
        locations[sym] = positions

# Look for antenna pairs, add antinode location if it exists
antinode_locations = set()
for sym in unique_antennas:
    pairs_list = list(combinations(locations[sym], r=2))

    for pairs in pairs_list:
        p1, p2 = pairs
        # Find distance apart
        rise = p2[0] - p1[0]
        run = p2[1] - p1[1]

        # Calculate antinode postion using distance apart
        antinode1 = [p1[0] - rise, p1[1] - run]
        antinode2 = [p2[0] + rise, p2[1] + run]

        # # Part 1 list of antinode locations
        # # Add antinode postion if it is in bounds and it doesn't already exist in set
        # if 0 <= antinode1[0] < h and 0 <= antinode1[1] < w:
        #     antinode_locations.add((antinode1[0], antinode1[1]))

        # if 0 <= antinode2[0] < h and 0 <= antinode2[1] < w:
        #     antinode_locations.add((antinode2[0], antinode2[1]))

        ###### Part 2 list of antinode locations ######
        # Add antinode postion if it is in bounds and it doesn't already exist in set
        antinode_locations.add(p1)
        antinode_locations.add(p2)
        while 0 <= antinode1[0] < h and 0 <= antinode1[1] < w:
            antinode_locations.add((antinode1[0], antinode1[1]))
            antinode1[0] -= rise
            antinode1[1] -= run

        while 0 <= antinode2[0] < h and 0 <= antinode2[1] < w:
            antinode_locations.add((antinode2[0], antinode2[1]))
            antinode2[0] += rise
            antinode2[1] += run
        
print(len(antinode_locations)) 



