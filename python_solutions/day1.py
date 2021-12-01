import os

totalIncreases = 0
lastInput = -1
allInputs = [-1]

# part 1
with open("../inputs/day1.txt", "r") as f:
    for line in f:
        allInputs.append(int(line))
        currentInput = int(line)
        if (lastInput > -1 and currentInput > lastInput):
            totalIncreases += 1
        lastInput = currentInput

print("Part 1 = {}".format(totalIncreases))

# part 2 - I know this could have been done in the above so we don't double loop...
totalIncreases = 0
ii = 1
while ii + 4 <= len(allInputs):
    first = sum(allInputs[ii : ii + 3])
    second = sum(allInputs[ii + 1 : ii + 4])
    #print("{} vs {}".format(first, second))
    if (second > first):
        totalIncreases += 1
    ii += 1

print("Part 2 = {}".format(totalIncreases))