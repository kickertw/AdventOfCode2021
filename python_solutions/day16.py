from utils import *
from collections import defaultdict

def getLiteralVal(input):
    literalBinaryVal = ''
    isLastGroup = False
    while True:
      isLastGroup = True if input[0] == '0' else False
      literalBinaryVal += input[1:5]
      input = input[5:]

      if isLastGroup:
        break
    
    # return the binary value and any remaining input
    return convertBinToDec(literalBinaryVal), input


def parsePacket(p, isHex = True):
  input = convertHexToBin(p) if isHex else p
  allValues = defaultdict(int)

  # If literal
  while len(input) > 0 and int(input) != 0:
    version = convertBinToDec(input[:3])
    typeId = convertBinToDec(input[3:6])
    if typeId == 4:
      #process literal values
      allValues[version], input = getLiteralVal(input[6:])
    else:
      lenTypeId = input[6]
      if lenTypeId == '0':
        totalLengthInBits = convertBinToDec(input[7:22])
        vals, input = parsePacket(input[22:22 + totalLengthInBits], False)
        for key in vals:
          allValues[key] = vals[key]
      else:
        #do nothing for now
        numberOfSubpackets = convertBinToDec(input[7:18])
        for _ in range(numberOfSubpackets):
          vals, input = parsePacket(input[18:], False)
          for key in vals:
            allValues[key] = vals[key]
  
  return allValues, input

vals, _ = parsePacket('A0016C880162017C3686B18A3D4780')
for key in vals:
  print(f'Version [{key}] = {vals[key]}')