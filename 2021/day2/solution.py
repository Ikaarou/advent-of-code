#!/usr/bin/env python3
file = open('input.txt',mode='r')
lines = file.read().splitlines()

coordinates = [0, 0]
for command in lines:
    direction, count = command.split()
    if direction == 'forward':
        coordinates[0] += int(count)
    elif direction == 'up':
        coordinates[1] -= int(count)
    elif direction == 'down':
        coordinates[1] += int(count)
print('Part 1:', coordinates[0] * coordinates[1])

aim = 0
coordinates = [0, 0]
for command in lines:
    direction, count = command.split()
    if direction == 'forward':
        coordinates[0] += int(count)
        coordinates[1] += aim * int(count)
    elif direction == 'up':
        aim -= int(count)
    elif direction == 'down':
        aim += int(count)


print('Part 2:', coordinates[0] * coordinates[1])