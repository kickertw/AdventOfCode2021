import os

totalIncreases = 0
lastInput = -1

# part 1
with open("./inputs/day1.txt", "r") as f:
    for line in f:
        currentInput = int(line)
        if (lastInput > -1 and currentInput > lastInput):
            totalIncreases += 1
        lastInput = currentInput    
        

print("Part 1 = {}".format(totalIncreases))