from collections import defaultdict

# No need to read in a txt file. Just change the input value since it's a single line of inputs
inputs = [int(x) for x in "1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1".split(',')]
lanternfish = defaultdict(int)
for idx, input in enumerate(inputs):
    lanternfish[idx] = input

# Part 1 + 2
days = 256
addCount = 0
newFishCountdownStart = 8
defaultCountdownStart = 6

fishCounts = [0] * 9
for ii in range(9):
    fishCounts[ii] = inputs.count(ii)

for x in range(days):
    #print(fishCounts)
    tempfishCounts = [0] * 9
    for ii in range(8, -1, -1):
        if ii == 0:
            tempfishCounts[8] = fishCounts[ii]
            tempfishCounts[6] += fishCounts[ii]
            continue
        
        if ii == 8:
            tempfishCounts[ii] = 0

        tempfishCounts[ii - 1] = fishCounts[ii]
    fishCounts = tempfishCounts.copy()

    if x == 80:
        print(f"Part 1 = {sum(fishCounts)}")
    
print(f"Part 2 = {sum(fishCounts)}")
