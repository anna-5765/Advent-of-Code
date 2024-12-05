## Day 3 - Mull it Over

import re

# Load input
with open("day3.txt", "r") as file:
    data = "do()" + file.read() + "don't()" # appending do and don't for part 2

# Use regular expressions to find cases in .txt that match mul(x,y) format
# Organize output to be able to access the numbers for processing
numbers1 = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

# Do math on those numbers to find total
def main(numbers):  
    total = 0
    for x,y in numbers:
        mult = int(x) * int(y)
        total += mult
    return total

total1 = main(numbers1)
print(total1) # part 1 answer

###### PART2 ######

# Find mul(x,y) between do() and don't() signals, include line breaks in regex dot
data2 = "".join(re.findall(r"do\(\)(.*?)don't\(\)", data, re.DOTALL))

# Organize output to access those x, y numbers
numbers2 = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data2)

total2 = main(numbers2)
print(total2) # part 2 answer


