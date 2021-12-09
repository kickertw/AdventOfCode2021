from utils import *
rawInputs = readFile('../inputs/day8.txt')

def getSignals(rawPatterns):
    signals = [None] * 10
    rawPatterns = si[0].rstrip().split()
    ambiguousPatterns = []
    for pattern in rawPatterns:
        pList = [letter for letter in pattern]
        if len(pList) == 2:
            signals[1] = pList
        elif len(pList) == 3:
            signals[7] = pList
        elif len(pList) == 4:
            signals[4] = pList
        elif len(pList) == 7:
            signals[8] = pList        
        ambiguousPatterns.append(pList)
    
    ii = 0
    topRightWire = ''
    pattern6Len = list(filter(lambda x: len(x) == 6, ambiguousPatterns))
    while len(pattern6Len) > 0:
        if (signals[6] == None and not listContains(signals[1], pattern6Len[ii])):
            signals[6] = pattern6Len[ii]
            if signals[1][0] not in signals[6]:
                topRightWire = signals[1][0]
            else:
                topRightWire = signals[1][1]
            del pattern6Len[ii]
            ii = 0
        elif (signals[9] == None and listContains(signals[4], pattern6Len[ii])):
            signals[9] = pattern6Len[ii]
            del pattern6Len[ii]
            ii = 0
        elif (signals[6] != None and signals[9] != None):
            signals[0] = pattern6Len[ii]
            del pattern6Len[ii]
        else:
            ii = 0 if ii == len(pattern6Len) - 1 else ii + 1

    pattern5Len = list(filter(lambda x: len(x) == 5, ambiguousPatterns))
    for pattern in pattern5Len:
        if (topRightWire in pattern):
            if (listContains(signals[1], pattern)):
                signals[3] = pattern
            else:
                signals[2] = pattern
        else:
            signals[5] = pattern
    
    return signals

def getSignalValue(signals, letters):
    idx = 0
    for s in signals:
        if len(letters) == len(s) and listContains(letters, s):
            return str(idx)
        idx += 1

p1Counter = 0
p2Sum = 0
for i in rawInputs:
    si = i.split('|')
    rawPatterns = si[0].rstrip().split()
    signals = getSignals(rawPatterns)
    
    # Part 1
    output = si[1].split()
    uniqueOutput = list(filter(lambda x: len(x) in [2,3,4,7], output))
    p1Counter += len(uniqueOutput)

    # Part 2
    val = ''    
    for o in output:
        oList = [letter for letter in o]
        signalVal = getSignalValue(signals, oList)
        #print(f'{o} == {signalVal}')
        val += signalVal
    p2Sum += int(val)

print(f'Part 1 = {p1Counter}')
print(f'Part 2 = {p2Sum}')