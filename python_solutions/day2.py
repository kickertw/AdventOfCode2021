import os

horizontal = 0
depth = 0

# part 1
with open("../inputs/day2.txt", "r") as f:
    for line in f:
        input = line.split()
        if (input[0] == 'forward'):
            horizontal += int(input[1])
        elif (input[0] == 'down'):
            depth += int(input[1])
        else:
            depth -= int(input[1])

print("Part 1 = {}".format(horizontal * depth))