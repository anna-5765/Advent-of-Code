# Day 7 - Bridge Repair

from itertools import product

# Load input
with open("day7.txt", "r") as file:
    data = [i.split(" ") for i in [line.strip() for line in file.readlines()]]
    
    for line in data:
        line[0] = line[0].rstrip(':')
        line[:] = [int(x) for x in line]

calibration = []

# for line in data:
#     check = line[0]
#     values = line[1:]

#     # Make combinations
#     for ops in product(['+', '*'], repeat=len(values)-1):
#         total = values[0]
#         for i, op in enumerate(ops):
#             if op == '+':
#                 total += values[i+1]
#             else: # op == '*'
#                 total *= values[i+1]
            
#         if total == check:
#             calibration.append(total)
#             break

###### PART 2 ######

for line in data:
    check = line[0]
    values = line[1:]

    # Make combinations
    for ops in product(['+', '*', '||'], repeat=len(values)-1):
        total = values[0]
        for i, op in enumerate(ops):
            if op == '+':
                total += values[i+1]
            elif op == '*':
                total *= values[i+1]
            else: # op == '||'
                total = int(str(total) + str(values[i+1]))
            
        if total == check:
            calibration.append(total)
            break

print(sum(calibration))