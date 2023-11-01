## Day 1

## Save input depth chart data to a list
filepath = '/Users/annaberghoff/Documents/code/AOC2021/day1.txt'
infile = open(filepath, 'r') # open file to read object
depth_data_r = infile.read() # store data from file in variable
depth_data_str = depth_data_r.split() # split data into list of strings
depth_data = [float(string) for string in depth_data_str] # convert list of strings to list of numbers
infile.close() # close file
# print(type(depth_data))

# print(depth_data)

## Calculate if the following datapiece has increased or decreased
depth_result = []

for i in range(len(depth_data)):
    if i == 0: # first measurement
        depth_result.append('na')
    previous = depth_data[i-1]
    # print(depth_data[i], previous)
    if depth_data[i] > previous: # measurement is greater than previous
        depth_result.append('increase')
    elif depth_data[i] < previous: # measurement is less than previous
        depth_result.append('decrease')
    else: # measurement is equal
        depth_result.append('equal')

# print(depth_result)
# print('The depth increases', depth_result.count('increase'), 'times')
# print('The depth decreases', depth_result.count('decrease'), 'times')

####### PART 2 #######

## Create new list with three measurement windows
depth_data_window = []

for i in range(len(depth_data)):
    depth_data_window.append(sum(depth_data[i:i+3]))

# print('Printing Window Sum!', depth_data_window)

## Evaluate whether data increases/decreases/no change
depth_w_result = []

for i in range(len(depth_data_window)):
    if i == 0: # first measurement
        depth_w_result.append('na')
    previous = depth_data_window[i-1]
    current = depth_data_window[i]
    if current > previous: # measurement is greater than previous
        depth_w_result.append('increase')
    elif current < previous: # measurement is less than previous
        depth_w_result.append('decrease')
    else: # measurement is equal
        depth_w_result.append('no change')

# print(depth_w_result)
print('The three term depth window increases', depth_w_result.count('increase'), 'times')