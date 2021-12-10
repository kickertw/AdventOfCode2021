from utils import *

def getP1Points(input):
    if input == ')':
        return 3
    elif input == ']':
        return 57
    elif input == '}':
        return 1197
    elif input == '>':
        return 25137

    return None

def getP2Points(inputs):
    missing = reversed(inputs)
    score = 0
    for item in missing:
        score *= 5
        if item == '(':
            score += 1
        elif item == '[':
            score += 2
        elif item == '{':
            score += 3
        elif item == '<':
            score += 4
    return score

rawInputs = readFile('../inputs/day10.txt')

openSyntax =  [ '(', '[', '{', '<']
closeSyntax = [')', ']', '}', '>']

p1PointTotal = 0
rii = 1
invalid = False
scoreList = []
for rawInput in rawInputs:
    chunkChecker = []
    chunkInput = [x for x in rawInput]
    for input in chunkInput:
        if len(chunkChecker) > 0:
            cidx = getIndexByVal(closeSyntax, input)
            if (cidx >= 0):
                lastVal = chunkChecker.pop()
                oidx = getIndexByVal(openSyntax, lastVal)
                if cidx != oidx:
                    print(f"{rii}. Expected {closeSyntax[oidx]}, but found {input} intead")
                    p1PointTotal += getP1Points(input)
                    invalid = True
                    break
            else:
                chunkChecker.append(input)
        else:
            chunkChecker.append(input)

    # For Debugging purposes        
    # if len(chunkChecker) == 0:
    #     print(f"{rii}. Legal Chunk - {''.join(chunkInput)}")
    # elif not invalid:
    #     print(f"{rii}. Incomplete Chunk")

    if len(chunkChecker) > 0 and not invalid:
        score = getP2Points(chunkChecker)
        print(f'{"".join(chunkChecker)} = {score}')
        scoreList.append(score)

    rii += 1
    invalid = False

print(f'Part 1 = {p1PointTotal}')

scoreList.sort()
print(f"Part 2 = {scoreList[len(scoreList)//2]}")