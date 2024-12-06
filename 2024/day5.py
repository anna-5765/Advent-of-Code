# Day 5 - Print Queue

from collections import defaultdict

# Load input
with open("day5.txt", "r") as file:
    # Split the input into page ordering rules and updates
    data = file.read().split("\n\n")
    # Rules is a list of tuples
    rules = [
        (int(a), int(b))
        for a, b in [rule.split("|") for rule in data[0].strip("\n").split("\n")]
    ]

    # Updates is a list of ordered pages
    updates = [
        [int(page) for page in update.split(",")]
        for update in data[1].strip("\n").split("\n")
    ]

"""
Given an input of updates and rules, 
specify which updates are in the correct order

the rules specify which pages must be listed before others

sum the middle number for correctly ordered updates
"""


# Create a dictionary for pages and what they must be ordered before
rules_dict = defaultdict(list)
for page, tail in rules:
    rules_dict[page].append(tail)


# Return True if update follows the rules, else False
def check_updates(update):
    previous = []
    # Loop through pages in an update
    for page in update:
        # Check if previous pages are allowed
        for prev in previous:
            if prev in rules_dict[page]:
                return False
        # Add current page to previous
        previous.append(page)
    return True


# Loop through updates and check their correctness
correct = []
incorrect = []  # added for part 2
for update in updates:
    if check_updates(update):
        correct.append(update)
    else:
        incorrect.append(update)


# Solve for the sum of the middle numbers in correct updates
def middle_sum(report):
    middle_numbers = []
    for update in report:
        index = int((len(update)) / 2)  # indicies start at 0 and ints truncate
        middle_numbers.append(update[index])
    return sum(middle_numbers)


total = middle_sum(correct)

print(total)  # part 1 answer


###### PART 2 ######

"""
Order the incorrect lists correctly

sum their middle numbers
"""


# Make a list of previous pages
def find_previous(index, update):
    previous = []
    for page in update[0:index]:
        previous.append(page)
    return previous


# Check rules and reorder pages appropriately
def check_rules(update):
    # Loop through pages in an update
    for page_index, page in enumerate(update):
        previous2 = find_previous(page_index, update)
        # Check if previous pages are allowed
        for prev_index, prev in enumerate(previous2):
            # If not allowed, insert value before
            if prev in rules_dict[page]:
                temp_list = previous2[prev_index:page_index]
                update[prev_index] = page
                update[(prev_index + 1) : (page_index + 1)] = temp_list
                # Check the new section for correctness
                check_rules(update[prev_index:page_index])
                break
    return update


# List fixed updates
correct2 = []
for update in incorrect:
    correct2.append(check_rules(update))

# Solve for their middle number sum
total2 = middle_sum(correct2)

print(total2)  # part 2 answer

###### part 2 using custom sort ######

from functools import cmp_to_key


def compare(a, b, rules=rules_dict):
    for before, afters in rules.items():
        if a == before and b in afters:
            return -1  # a should come before b
        if b == before and a in afters:
            return 1  # b should come before a
    return 0


# Sort using custom rules for pairwise comparison
sorted_updates = [sorted(update, key=cmp_to_key(compare)) for update in incorrect]

# is this the same as previous part 2 answer? Yes it is
total3 = middle_sum(sorted_updates)
if total3 == total2:
    print("True")
else:
    print("False")
