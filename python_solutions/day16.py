from utils import *
from collections import defaultdict

def parseLiteral(version, input, level):
  global packetValues

  print(f'Parsing Literal [Level = {level}]')
  literalBinaryVal = ''
  isLastGroup = False
  while True:
    isLastGroup = True if input[0] == '0' else False
    literalBinaryVal += input[1:5]
    input = input[5:]

    if isLastGroup:
      break
  
  decVal = convertBinToDec(literalBinaryVal)
  packetValues[version].append(decVal)
  print('DONE Parsing')
  #return any remaining input  
  return input

def parseOperator(input, level):
  print(f'Parsing Operator [Level = {level}]')
  lTypeId = input[0]
  lbits = 15 if lTypeId == '0' else 11

  input = input[1:]
  lengthVal = convertBinToDec(input[:lbits])
  if lTypeId == '0':    
    input1 = input[lbits:lbits+lengthVal]
    input2 = input[lbits+lengthVal:]
    while len(input1) > 0 and int(input1) > 0:
      input1 = parsePacket(input1, level+1)

    if len(input2) > 0 and int(input2) > 0:
      input = parsePacket(input2, level+1)
  else:
    input = input[lbits:]
    for _ in range(lengthVal):
      input = parsePacket(input, level+1)

  print(f'DONE Parsing Operator [Level = {level}]')
  return input  

def parsePacket(input, level = 0):
  global versionSum

  if len(input) == 0 or int(input) == 0:
    return ''

  print(f'Parsing Packet [Level = {level}]')
  version = convertBinToDec(input[:3])
  typeId = convertBinToDec(input[3:6])
  print(f'Version Found! [{input[:3]} = {version}]')
  versionSum += version
  # If literal
  if typeId == 4:
    # while len(input) > 0 and int(input) > 0:
    typeId = convertBinToDec(input[3:6])
    input = parseLiteral(version, input[6:], level)
  else:
    input = input[6:]
    input = parseOperator(input, level + 1)
  print(f'Done Parsing Packet [Level = {level}]')
  return input

versionSum = 0
packetValues = defaultdict(list)
binVal = convertHexToBin('A0016C880162017C3686B18A3D4780')
parsePacket(binVal)

print(f'Literal Val count = {len(packetValues.keys())}')
print(f'Version Sum = {versionSum}')