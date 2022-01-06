import math
import re
from utils import *

def addFish(left, right):
  retVal = f'[{left},{right}]'
  return retVal

def findAndExplode(input):
  nestLevel = 0
  ii = 0
  newInput = ''

  while ii < len(input):
    if input[ii] == '[':
      nestLevel += 1
    
    if input[ii] == ']':
      nestLevel -= 1

    if nestLevel >= 5:
      pairToExplode = re.search('\[\d+,\d+\]', input[ii:]) 
      if pairToExplode != None:
        pStart, pEnd = pairToExplode.span()
        pairs = input[ii+pStart+1:ii+pEnd-1].split(',')
        leftNum = int(pairs[0])
        rightNum = int(pairs[1])

        #The number before the nested range
        priorNumberMatches = list(re.finditer('\d+', input[:ii+pStart]))
        if priorNumberMatches:
          priorStart, priorEnd = priorNumberMatches[-1].span()
          newPriorNumber = int(input[priorStart:priorEnd]) + leftNum
          newInput = input[:priorStart] + str(newPriorNumber) + input[priorEnd:ii+pStart] + '0'
        else:
          newInput = input[:ii+pStart] + '0'

        #The number after the nested range
        nextNumberMatch = re.search('\d+', input[ii+pEnd:])
        if nextNumberMatch:
          nextStart, nextEnd = nextNumberMatch.span()
          newNextNumber = int(input[ii+pEnd+nextStart:ii+pEnd+nextEnd]) + rightNum
          newInput += input[ii+pEnd:ii+pEnd+nextStart] + str(newNextNumber) + input[ii+pEnd+nextEnd:]
        else:
          newInput += input[ii+pEnd:]
      
        return newInput

    ii += 1

  # If nothing to explode, return original input
  return input

def findAndSplit(input):
  for match in re.finditer('\d+', input):
    matchVal = int(match.group())
    if matchVal > 9:
      start, end = match.span()
      return input[:start] + f'[{math.floor(matchVal/2)},{math.ceil(matchVal/2)}]' + input[end:]
  
  # Return if nothing to split
  return input

def reduce(input):
  lastInput = ''
  while lastInput != input:
    lastInput = input
    input = findAndExplode(input)
    if lastInput != input:
      continue

    input = findAndSplit(input)

  return input

def getMagnitude(input):
  match = re.search('\[\d+,\d+\]', input)
  while match != None:
    start, end = match.span()
    vals = input[start+1:end-1].split(',')
    newVal = 3*int(vals[0]) + 2*int(vals[1])
    input = input[:start] + str(newVal) + input[end:]
    match = re.search('\[\d+,\d+\]', input)
  
  return int(input)

rawInputs = readFile('./inputs/day18.txt')
input = rawInputs[0]
for ii in range(1, len(rawInputs)):
  input = addFish(input, rawInputs[ii])
  input = reduce(input)

magnitude = getMagnitude(input)
print(f'Part 1 = {magnitude}')

highestMag = 0
for ii in range(len(rawInputs)):
  for jj in range(len(rawInputs)):
    if ii != jj:
      input = addFish(rawInputs[ii], rawInputs[jj])
      input = reduce(input)

      magnitude = getMagnitude(input)
      highestMag = magnitude if magnitude > highestMag else highestMag

print(f'Part 2 = {highestMag}')

