import os

def binaryToDecimal(n):
    return int(n,2)

def readFile(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]    
    return lines

def countOnesZeros(inputs):
    ones = [0]
    zeroes = [0]
    for input in inputs:
        # initialize the list size
        if (len(ones) == 1):            
            ones = [0] * (len(input))
            zeroes = [0] * (len(input))

        ii = 0
        for character in input:
            if (character == '0'):
                zeroes[ii] += 1
            else:
                ones[ii] += 1
            ii += 1
    return ones, zeroes

def findXCommonBit(mode, inputs, pos):
    oneCount = 0
    zeroCount = 0
    retVal = '1' if mode == 'most' else '0'

    for input in inputs:
        if (input[pos] == '0'):
            zeroCount += 1
        else:
            oneCount += 1
    
    if mode == 'most':
        if oneCount > zeroCount:
            retval = '1'
        elif zeroCount > oneCount:
            retVal = '0'
    else:
        if oneCount > zeroCount:
            retval = '0'
        elif zeroCount > oneCount:
            retVal = '1'

    return retVal

# part 1
inputs = readFile("../inputs/day3.txt")
ones, zeroes = countOnesZeros(inputs)

gamma = [''] * (len(ones))
epsillon = [''] * (len(ones))

for ii in range(len(gamma)):
    gamma[ii] = '1' if ones[ii] > zeroes[ii] else '0'
    epsillon[ii] = '1' if zeroes[ii] > ones[ii] else '0'

gammaVal = binaryToDecimal(''.join(gamma))
epsillonVal = binaryToDecimal(''.join(epsillon))

print("Part 1 = {} * {} = {}".format(gammaVal, epsillonVal, gammaVal * epsillonVal))

# part 2
maxLen = len(inputs[0])
oldList = inputs.copy()
tempList = []
ii = 0

# o2Rating
while len(oldList) > 1:
    mcb = findXCommonBit('most', oldList, ii)
    for item in oldList:
        if (item[ii] == mcb):
            tempList.append(item)

    oldList = tempList
    tempList = []
    ii += 1
o2Rating = oldList[0]

# co2Rating
ii = 0
oldList = inputs.copy()
while len(oldList) > 1:
    lcb = findXCommonBit('least', oldList, ii)
    for item in oldList:
        if (item[ii] == lcb):
            tempList.append(item)

    oldList = tempList
    tempList = []
    ii += 1
co2Rating = oldList[0]

o2RatingVal = binaryToDecimal(''.join(o2Rating))
co2RatingVal = binaryToDecimal(''.join(co2Rating))
print("Part 2 = {} * {} = {}".format(o2RatingVal, co2RatingVal, o2RatingVal * co2RatingVal))