from utils import *
from collections import defaultdict

def parseLiteral(version, input, level):
  global packetValues
  global debug
  spaces = '  ' * level

  literalBinaryVal = ''
  isLastGroup = False
  subPacketCount = 0
  while True:
    isLastGroup = True if input[0] == '0' else False
    literalBinaryVal += input[1:5]
    input = input[5:]
    subPacketCount += 1
    if isLastGroup:
      break
  
  decVal = convertBinToDec(literalBinaryVal)
  debugPrint(debug, f'{spaces} Parsing Literal [V = {version} / # of Subpackets = {subPacketCount} / {literalBinaryVal} = {decVal}]')
  packetValues[version].append(decVal)
  #return any remaining input  
  return input

def parseOperator(input, level):
  global debug

  spaces = '  ' * level
  lTypeId = input[0]
  lbits = 15 if lTypeId == '0' else 11

  input = input[1:]
  lengthVal = convertBinToDec(input[:lbits])
  lengthTypeDebug = 'packets' if lTypeId == '1' else 'bits'
  debugPrint(debug, f'{spaces} I = {lTypeId} / L = has {lengthVal} {lengthTypeDebug}')
  if lTypeId == '0':
    #we know the number of bits to look at
    input1 = input[lbits:lbits+lengthVal]
    while len(input1) > 0 and int(input1) > 0:
      input1 = parsePacket(input1, level+1)

    input = input[lbits+lengthVal:]
  else:
    #we know the number of packets
    input = input[lbits:]
    for _ in range(lengthVal):
      input = parsePacket(input, level+1)
  return input  

def parsePacket(input, level = 0):
  global versionSum
  global debug
  spaces = '  ' * level

  if len(input) == 0 or int(input) == 0:
    return ''

  version = convertBinToDec(input[:3])
  typeId = convertBinToDec(input[3:6])
  versionSum += version
  # If literal
  if typeId == 4:    
    debugPrint(debug, f'{spaces} Literal Found! Version={version}')
    input = parseLiteral(version, input[6:], level)
  else:
    input = input[6:]
    debugPrint(debug, f'{spaces} Operator Found! Version={version}')
    input = parseOperator(input, level)
  return input

versionSum = 0
debug = False
packetValues = defaultdict(list)
binVal = convertHexToBin('420D5A802122FD25C8CD7CC010B00564D0E4B76C7D5A59C8C014E007325F116C958F2C7D31EB4EDF90A9803B2EB5340924CA002761803317E2B4793006E28C2286440087C5682312D0024B9EF464DF37EFA0CD031802FA00B4B7ED2D6BD2109485E3F3791FDEB3AF0D8802A899E49370012A926A9F8193801531C84F5F573004F803571006A2C46B8280008645C8B91924AD3753002E512400CC170038400A002BCD80A445002440082021DD807C0201C510066670035C00940125D803E170030400B7003C0018660034E6F1801201042575880A5004D9372A520E735C876FD2C3008274D24CDE614A68626D94804D4929693F003531006A1A47C85000084C4586B10D802F5977E88D2DD2898D6F17A614CC0109E9CE97D02D006EC00086C648591740010C8AF14E0E180253673400AA48D15E468A2000ADCCED1A174218D6C017DCFAA4EB2C8C5FA7F21D3F9152012F6C01797FF3B4AE38C32FFE7695C719A6AB5E25080250EE7BB7FEF72E13980553CE932EB26C72A2D26372D69759CC014F005E7E9F4E9FA7D3653FCC879803E200CC678470EC0010E82B11E34080330D211C663004F00101911791179296E7F869F9C017998EF11A1BCA52989F5EA778866008D8023255DFBB7BD2A552B65A98ECFEC51D540209DFF2FF2B9C1B9FE5D6A469F81590079160094CD73D85FD2699C5C9DCF21F0700094A1AC9EDA64AE3D37D34200B7B401596D678A73AFB2D0B1B88057230A42B2BD88E7F9F0C94F1ECB7B0DD393489182F9802D3F875C00DC40010F8911C61F8002111BA1FC2E400BEA5AA0334F9359EA741892D81100B83337BD2DDB4E43B401A800021F19A09C1F1006229C3F8726009E002A12D71B96B8E49BB180273AA722468002CC7B818C01B04F77B39EFDF53973D95ADB5CD921802980199CF4ADAA7B67B3D9ACFBEC4F82D19A4F75DE78002007CD6D1A24455200A0E5C47801559BF58665D80')
parsePacket(binVal)

print(f'Version Sum = {versionSum}')