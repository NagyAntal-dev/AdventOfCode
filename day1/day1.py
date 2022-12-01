### Day 1 ###
import operator

data = open("input.txt","r")
lines = [int(item.strip()) if item.strip() != '' else item.strip() for item in data.readlines()]

### Part 1 ###
elves = []
all_calories = 0

for line in lines:
    if line != '':
        all_calories += line
    else:
        elves.append(all_calories)
        all_calories = 0

print("Part 1: " + str(max(elves)))

### Part 2 ###
elves = sorted(elves, reverse=True)
print("Part 2: " + str( elves[0] + elves[1] + elves[2] ))