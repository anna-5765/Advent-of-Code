## Day 1 - Historian Hysteria

import numpy as np

data = np.loadtxt("day1.txt")  # load data
left_list = np.sort(data[:, 0])  # split columns and sort least to greatest
right_list = np.sort(data[:, 1])

distance = 0

# Find the total distance between the lists
# in this case the distance is the sum of the difference between the two items in each list
for x, y in zip(left_list, right_list):
    distance += abs(x - y)

# print(distance) # part 1 answer

###### PART 2 ######

count = 0
sim_score = 0

# Solve for the similarity score
for x in left_list:
    for y in right_list:
        if x == y:
            count += 1
    sim_score += x * count
    count = 0

print(sim_score) # part 2 answer
