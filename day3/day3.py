from string import ascii_lowercase
from string import ascii_uppercase

### With sets get back the common item ###
def commonItem(backpack):
    firstHalf = set(backpack[:len(backpack)//2])
    secondHalf = set(backpack[len(backpack)//2:])
    return list(set.intersection(firstHalf,secondHalf))

### Check if its a group of three ###
def isGroup(first, second, third):
    first = set(first)
    second = set(second)
    third = set(third)

    if(len(set.intersection(first,second,third)) != 0):
        return True
    else:
        return False

### Get Badge of the group
def getBadge(first, second, third):
    first = set(first)
    second = set(second)
    third = set(third)

    return list(set.intersection(first,second,third))[0]

### Here are our priors by characters ###
priority_table = dict([(v,i+1) for i,v in enumerate(ascii_lowercase+ascii_uppercase)])

### Process Input ###
data = open('input.txt','r')
lines = [line.strip() for line in data.readlines()]

### Part 1 ###
ans = 0
for line in lines:
    tmp = commonItem(line)
    for i in tmp:
        ans += priority_table[i]

print('Part 1: ' + str(ans))

### Part 2 ###
ans = 0
for i in range(0,len(lines),3):
    ans += priority_table[getBadge(lines[i],lines[i+1],lines[i+2])]

print('Part 2: ' + str(ans))