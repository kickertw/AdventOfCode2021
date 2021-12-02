import os

horizontal = 0
p1depth = 0
p2depth = 0
aim = 0

# part 1
with open("../inputs/day2.txt", "r") as f:
    for line in f:
        input = line.split()
        if (input[0] == 'forward'):
            horizontal += int(input[1])
            p2depth += aim * int(input[1])
        elif (input[0] == 'down'):
            p1depth += int(input[1])
            aim += int(input[1])
        else:
            p1depth -= int(input[1])
            aim -= int(input[1])


print("Part 1 = {}".format(horizontal * p1depth))
print("Part 2 = {}".format(horizontal * p2depth))