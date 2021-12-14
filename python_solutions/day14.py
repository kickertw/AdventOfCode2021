import sys
from utils import *
from collections import defaultdict

def stepAndCount(pairCounts, rules, singleLetterCounts):
  newPairCounts = dict.fromkeys(rules, 0)

  for key in pairCounts:
    # Get the number of pairs we need to get a new letter for
    oldCount = pairCounts[key]

    # Get the new letter and increment the count
    newLetter = rules[key]
    singleLetterCounts[newLetter] += oldCount

    # Save the new pairs and the number of times they're occurring
    newPair1 = key[0] + newLetter
    newPair2 = newLetter + key[1]
    newPairCounts[newPair1] += oldCount
    newPairCounts[newPair2] += oldCount    
  
  return newPairCounts

def getHighLow(singleLetterCounts):
  highCount = 0
  lowCount = sys.maxsize

  for key in singleLetterCounts.keys():
    highCount = singleLetterCounts[key] if highCount < singleLetterCounts[key] else highCount
    lowCount = singleLetterCounts[key] if lowCount > singleLetterCounts[key] else lowCount
  
  return lowCount, highCount

rawInputs = readFile('../inputs/day14.txt')

template = ''
rules = defaultdict(str)
for idx, input in enumerate(rawInputs):
  if idx == 0:
    template = input
    continue

  if idx > 1:
    rule = input.split(' -> ')
    rules[rule[0]] = rule[1]

# Pair counting
singleLetterCounter = defaultdict(int)
for char in template:
  singleLetterCounter[char] += 1

pairCounter = defaultdict(int)
for ii in range(len(template)-1):
  pairCounter[template[ii:ii+2]] += 1

steps = 40
for ii in range(steps):
  filteredCounter = dict(filter(lambda kvp: kvp[1] > 0, pairCounter.items()))
  pairCounter = stepAndCount(filteredCounter, rules, singleLetterCounter)
  if ii == 9:
    lowCount, highCount = getHighLow(singleLetterCounter)
    print(f"Part 1 = {(highCount - lowCount)}")

lowCount, highCount = getHighLow(singleLetterCounter)
print(f"Part 2 = {(highCount - lowCount)}")