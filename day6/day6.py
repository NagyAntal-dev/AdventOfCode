### Data Processing ###
signal = open('input.txt','r').readline().strip()

### Part 1 ###
i = 0
while i <= len(signal)-4 and len(set(signal[i:i+4])) != 4:
    i+=1

print('Part 1: ' + str(i+4))

### Part 2 ###
i = 0
while i <= len(signal)-14 and len(set(signal[i:i+14])) != 14:
    i+=1

print('Part 2: ' + str(i+14))