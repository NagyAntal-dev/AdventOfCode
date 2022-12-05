import re
import copy

### Generates a dict of the input ###
def getStackDict(ware):
    result = dict([(i+1,[]) for i in range(len(ware[0]))])
    for line in ware:
        for i,v in enumerate(line):
            if v[1] != ' ':
                result[i+1].append(v[1])
    return result

### Command is processed from line ###
def doCommand(ware, command):
    for i,v in enumerate(command):
        command[i] = int(v)
    
    ware[command[2]] = ware[command[1]][:command[0]][::-1] + ware[command[2]]
    ware[command[1]] = ware[command[1]][command[0]:]
    return ware

### Command is processed from line but not reversed###
def doCommandHolds(ware, command):
    for i,v in enumerate(command):
        command[i] = int(v)
    
    ware[command[2]] = ware[command[1]][:command[0]] + ware[command[2]]
    ware[command[1]] = ware[command[1]][command[0]:]
    return ware


### Process Data ###
inputText = 'input.txt'
data = [re.sub('\s\s\s\s',' [ ] ',item.replace("\n", "")).strip() for item in open(inputText,'r').readlines()]
warehouse = []
warehouse2 = []
i = 0
while i <= len(data) and data[i+1] != '':
    tmp = re.findall('\[\w\]|\[\W\]',data[i])
    warehouse.append(tmp)
    i += 1

### Get the warehouse ###
warehouse = getStackDict(warehouse)
warehouse2 = copy.deepcopy(warehouse)

### Part 1-2: Do the commands ###
i += 2
while i <= len(data)-1:
    warehouse = doCommand(warehouse,re.findall('\d{1,}',data[i]))
    warehouse2 = doCommandHolds(warehouse2,re.findall('\d{1,}',data[i]))
    i+=1

print('Part 1:')
for i,v in enumerate(warehouse):
    print(warehouse[i+1][0], end='')
print()
print('Part 2:')
for i,v in enumerate(warehouse2):
    print(warehouse2[i+1][0], end='')
print()