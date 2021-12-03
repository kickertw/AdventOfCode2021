import os

def binaryToDecimal(n):
    return int(n,2)

ones = [0]
zeroes = [0]

# part 1
with open("../inputs/day3.txt", "r") as f:
    for line in f:
        input = list(line)

        # initialize the list size
        if (len(ones) == 1):            
            ones = [0] * (len(input)-1)
            zeroes = [0] * (len(input)-1)

        ii = 0
        for character in input:
            if (character == '0'):
                ones[ii] += 1
            elif (character == '1'):
                zeroes[ii] += 1
            ii += 1

gamma = [''] * (len(ones))
epsillon = [''] * (len(ones))

for ii in range(len(gamma)):
    gamma[ii] = '1' if ones[ii] > zeroes[ii] else '0'
    epsillon[ii] = '1' if zeroes[ii] > ones[ii] else '0'

gammaVal = binaryToDecimal(''.join(gamma))
epsillonVal = binaryToDecimal(''.join(epsillon))

print("Part 1 = {} * {} = {}".format(gammaVal, epsillonVal, gammaVal * epsillonVal))
