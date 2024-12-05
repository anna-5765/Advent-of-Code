# Day 4 - Ceres Search

# Load input
with open("day4.txt", "r") as file:
    # Make the crossword puzzle a 2d matrix that is a list of letters for each line
    puzzle = [[char for char in line.rstrip('\n')] for line in file.readlines()]

# Find puzzle size
height = len(puzzle)
width = len(puzzle[0])

# Create valid search terms
xmas = ['X', 'M', 'A', 'S']
xmas_b = ['S', 'A', 'M', 'X']
xmas_v = [['X'], ['M'], ['A'], ['S']]
xmas_vb = [['S'], ['A'], ['M'], ['X']]

# Loop through puzzle letters for horizonal searches
count = 0
for i in range(0, height):
    for j in range(0, width - 3):
        # Create search area
        check_h = [puzzle[i][j], puzzle[i][j+1], puzzle[i][j+2], puzzle[i][j+3]]
               
        # Search horizontal
        if check_h == xmas:
            count += 1
        if check_h == xmas_b:
            count += 1

# Loop through puzzle letters for vertical searches
for j in range(0, width):
    for i in range(0, height - 3):
        # Create search area
        check_v = [[puzzle[i][j]],
                   [puzzle[i+1][j]],
                   [puzzle[i+2][j]],
                   [puzzle[i+3][j]]]
        
        # Search vertical
        if check_v == xmas_v:
            count += 1
        if check_v == xmas_vb:
            count += 1

# loop through puzzle letters for diagonal search
for i in range(0, height - 3):
    for j in range(0, width - 3):
        # Create search area
        check_d_lr = [[puzzle[i][j]],
                      [puzzle[i+1][j+1]],
                      [puzzle[i+2][j+2]],
                      [puzzle[i+3][j+3]]]
        
        check_d_rl = [[puzzle[i][j+3]],
                      [puzzle[i+1][j+2]],
                      [puzzle[i+2][j+1]],
                      [puzzle[i+3][j]]]
        
        # Search diagonal
        if check_d_lr == xmas_v:
            count += 1
        if check_d_rl == xmas_v:
            count += 1
        if check_d_lr == xmas_vb:
            count += 1
        if check_d_rl == xmas_vb:
            count += 1
        
print(count) # part 1 answer

###### PART 2 ######

# Create valid search terms
mas_f = [['M'], ['A'], ['S']]
mas_b = [['S'], ['A'], ['M']]

# Loop through puzzle letters for x-mas search
count2 = 0
for i in range(0, height - 2):
    for j in range(0, width - 2):
        # Create search area
        m_check_d_lr = [[puzzle[i][j]],
                        [puzzle[i+1][j+1]],
                        [puzzle[i+2][j+2]]]
        
        m_check_d_rl = [[puzzle[i][j+2]],
                        [puzzle[i+1][j+1]],
                        [puzzle[i+2][j]]]
        
        # Search x-mas
        condition1 = m_check_d_lr == mas_f or m_check_d_lr == mas_b
        condition2 = m_check_d_rl == mas_f or m_check_d_rl == mas_b
        
        if condition1 and condition2:
            count2 += 1

print(count2) # part 2 answer