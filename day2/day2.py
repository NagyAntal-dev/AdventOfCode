from enum import Enum
### Enum for points ###
class PointTable(Enum):
    A = 1
    B = 2
    C = 3
    D = 3
    W = 6
    L = 0

## Get points ###
def getPoints(opponet, elf):
    round = 0
    elf = elf.replace('X','A').replace('Y','B').replace('Z','C')
    if opponet == elf:
        round += PointTable['D'].value + PointTable[elf].value
        return round

    elif opponet == 'A' and elf == 'B':
        round += PointTable['W'].value + PointTable[elf].value
        return round

    elif opponet == 'A' and elf == 'C':
        round += PointTable['L'].value + PointTable[elf].value
        return round

    elif opponet == 'B' and elf == 'A':
        round += PointTable['L'].value + PointTable[elf].value
        return round

    elif opponet == 'B' and elf == 'C':
        round += PointTable['W'].value + PointTable[elf].value
        return round

    elif opponet == 'C' and elf == 'A':
        round += PointTable['W'].value + PointTable[elf].value
        return round

    elif opponet == 'C' and elf == 'B':
        round += PointTable['L'].value + PointTable[elf].value
        return round

### Calculate the round ###
def CalcTheRound(oppent, elf):
    winner = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    loser = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    if elf == 'X':
        elf = loser[oppent]
    elif elf == 'Y':
        elf = draw[oppent]
    elif elf == 'Z':
        elf = winner[oppent]

    return getPoints(oppent, elf)

### Process Data ###
data = open('input.txt','r')
lines = [item.strip().split(' ') for item in data.readlines()]

### Part 1 ###
points = 0
for item in lines:
    points += getPoints(item[0], item[1])

print("Part 1: " + str(points))

### Part 2 ###
points = 0
for item in lines:
    points += CalcTheRound(item[0], item[1])

print("Part 2: " + str(points))