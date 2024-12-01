## Day 3
import numpy as np

## Save input diagnostic report to a list using numpy
filepath = '/Users/annaberghoff/Documents/code/AOC2021/day3.txt'
diag_data = np.loadtxt(filepath, dtype = str)

## Find most and least common bit for each place
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # initialize bit counter array
for num in diag_data:
    for bit in range(len(num)):
        if num[bit]== '1': 
            count[bit] += 1 # count number of 1s in each column

## Find gamma rate (most common bit) and epsilon rate (least common bit)
gamma_rate = ""
epsilon_rate = "" 
for i in range(len(count)):
    if count[i] > len(diag_data)/2: # 1 is most common if count is greater than half of total
        gamma_rate += '1'
        epsilon_rate += '0'
    else: 
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_d = int(gamma_rate, 2) # convert to decimal
epsilon_d = int(epsilon_rate, 2) # convert to decimal

# print(gamma_rate)        
## Find epsilon rate (least common bit in each place and inverse of gamma)
# epsilon_rate = ""
# for i in gamma_rate:
#     if i == '1':
#         epsilon_rate += '0'
#     else: epsilon_rate += '1'


## Find power consumption (multiply gamma and epsilon decimals)
power = gamma_d * epsilon_d
print(power) 

####### Part 2 #######

## Find oxygen generator rating (keep only the numbers with the most common value of bit)
oxygen_gen = []
for i in range(12):
    oxygen_gen.append([])


# Make count function to use for both
def count(input_array, bit):
    ones = 0
    zeros = 0
    for num in input_array[bit-1]:
        if num[bit] == '0':
            zeros += 1
        else:
            ones += 1
    return ones, zeros

    
for bit in range(len(diag_data[0])):
   if bit == 0:
        for num in diag_data:
            if num[bit] == gamma_rate[bit]:
                oxygen_gen[bit].append(num)
   else:
        for each in oxygen_gen[bit-1]:
            ones, zeros = count(oxygen_gen, bit)
            if ones > zeros:
                if each[bit] == '1':
                    oxygen_gen[bit].append(each)
            elif zeros > ones:
                if each[bit] == '0':
                    oxygen_gen[bit].append(each)
            else: 
                if each[bit] == '1':
                    oxygen_gen[bit].append(each)

print(oxygen_gen[11]) # one number left

## Find C02 scrubber rating (keep only the numbers with the least common values, zero if equal)
co2_scrub = []
for i in range(12):
    co2_scrub.append([])

for bit in range(len(diag_data[0])):
   if bit == 0:
        for num in diag_data:
            if num[bit] == epsilon_rate[bit]:
                co2_scrub[bit].append(num)
   else:
        for each in co2_scrub[bit-1]:
            ones, zeros = count(co2_scrub, bit)
            if ones > zeros:
                if each[bit] == '0':
                    co2_scrub[bit].append(each)
            elif zeros > ones:
                if each[bit] == '1':
                    co2_scrub[bit].append(each)
            else: 
                if each[bit] == '0':
                    co2_scrub[bit].append(each)
        
print(co2_scrub[8]) # one number left

## Solve by multiplying oxy and co2 decimals

print("life support rating is", int(oxygen_gen[11][0],2)*int(co2_scrub[8][0],2))