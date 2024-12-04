## Day 2 - Red-Nosed Reports

# Load input
with open("day2.txt", "r") as file:
    # Data is a list of reports, each report a list of levels
    data = []
    for index, line in enumerate(file):
        data.insert(index, [int(x) for x in line.split()])

# Initialize safety variables
safe = 0
unsafe = 0


# Check if subsequent numbers are increasing or decreasing
def check_status(variance):
    if variance > 0:
        return "decreasing"
    else:
        return "increasing"


# Check safety of report
def check_safety(report):
    # Loop through levels of report
    for j, level in enumerate(report):
        if j == 0:
            continue
        else:
            # Check appropriate variance
            var1, var2 = level, report[j - 1]
            variance = var1 - var2
            if abs(variance) < 1 or abs(variance) > 3:
                return False
            else:
                if j == 1:
                    status = check_status(variance)
                else:
                    # Ensure gradual increase/decrease across all levels
                    new_status = check_status(variance)
                    if new_status != status:
                        return False
                if j == len(report) - 1:
                    if new_status == status:
                        return True


unsafe_list = []  # used for part 2
# Calculate number of safe reports
for report in data:
    safety = check_safety(report)
    if safety:
        safe += 1
    else:
        unsafe += 1
        unsafe_list.append(report)  # used for part 2

print(safe)  # part 1 answer

###### PART 2 ######

# Initialize new safety variables
p2_safe = 0
p2_unsafe = 0

# Loop through reports in the previous unsafe list
for report in unsafe_list:
    for index, level in enumerate(report):
        report_copy = report.copy()  # make a copy of report
        report_copy.pop(index)  # check to see if safe with one level removed
        safety = check_safety(report_copy)
        if safety:
            p2_safe += 1
            break
        else:
            p2_unsafe += 1

print(p2_safe + safe)  # part 2 answer
