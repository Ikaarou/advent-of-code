#!/usr/bin/env python3

file = open('input.txt',mode='r')

elves = [0]
lines = file.readlines()

count = 0
elves_id = 0
# Strips the newline character
for line in lines:
    content = line.strip()
    if content == '':
        elves.append(0)
        elves_id += 1
    else:
        value = elves[elves_id] + int(content)
        elves[elves_id] = value

elves.sort(reverse=True)
print(len(elves))
#1
print('Max', max(elves))
#2
print('Top3', elves[0] + elves[1] + elves[2])

# close the file
file.close()