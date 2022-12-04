### Get intersection of two cleaning ###
def getIntersection(first,second):
    sizeOfCamp = [i for i in range(1,100)]
    first_tmp = getRangeOfElf(first)
    first = sizeOfCamp[first_tmp[0]:first_tmp[1]]
    first_tmp = getRangeOfElf(second)
    second = sizeOfCamp[first_tmp[0]:first_tmp[1]]
    return(set.intersection(set(first),set(second)))

### Check if Pairs are fully contained ###
def isFullyContained(first,second):
    sizeOfCamp = [i for i in range(1,100)]
    first_tmp = getRangeOfElf(first)
    first = set(sizeOfCamp[first_tmp[0]:first_tmp[1]])
    first_tmp = getRangeOfElf(second)
    second = set(sizeOfCamp[first_tmp[0]:first_tmp[1]])

    if len(first) > len(second):
        return second.issubset(first)
    else:
        return first.issubset(second)

### Get range of the elf ###
def getRangeOfElf(elf):
    x = [int(elf.split('-')[0])-1,int(elf.split('-')[1])]
    return(x)

### Data processing ###
lines = [item.strip().split(',') for item in open('input.txt','r').readlines()]
print(isFullyContained(lines[3][0], lines[3][1]))

### Part 1 ###
numberOfContains = 0
for pairs in lines:
    if isFullyContained(pairs[0],pairs[1]):
        numberOfContains+=1

print('Part 1: ' + str(numberOfContains))

### Part 2 ###
numberOfContains = 0
for pairs in lines:
    if isFullyContained(pairs[0],pairs[1]) or len(getIntersection(pairs[0],pairs[1])) != 0:
        numberOfContains+=1

print('Part 2: ' + str(numberOfContains))