## Day 2
import numpy as np

## Save input directional data (numbers and string) to a list using numpy
dir_data = np.genfromtxt('AOC2021/day2.txt', delimiter=' ', dtype=['U10',int]).tolist()
# print(dir_data)

depth = 0 # initialize depth
h_pos = 0 # initialize horizontal pos
for i in range(len(dir_data)):
    if dir_data[i][0] == 'down':
        depth += dir_data[i][1]
    elif dir_data[i][0] == 'up':
        depth -= dir_data[i][1]
    elif dir_data[i][0] == 'forward':
        h_pos += dir_data[i][1]
    else:
        print('not in if statements')

# print('horizonal position', h_pos)  
# print('depth', depth)  

# print('Multiply answers', h_pos*depth)

####### Part 2 #######

depth_2 = 0 # initialize depth part 2
h_pos_2 = 0 # initialize horizontal pos part 2
aim = 0 # initialize aim
for i in range(len(dir_data)):
    if dir_data[i][0] == 'down':
        aim += dir_data[i][1]
    elif dir_data[i][0] == 'up':
        aim -= dir_data[i][1]
    elif dir_data[i][0] == 'forward':
        h_pos_2 += dir_data[i][1]
        depth_2 += aim * dir_data[i][1]
    else:
        print('not in if statements')

print('Multiply answers part 2', h_pos*depth_2)