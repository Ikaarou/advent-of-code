#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

cycles = [1]
def get_required_cycles_sum(cycles, required):
    def get_index(i):
        return cycles[i - 1] * i
    return sum(map(get_index, required))

for line in lines:
    command = line.split()
    last_element = cycles[len(cycles) - 1]
    if command[0] == 'noop':
        cycles.append(last_element)
    else:
        cycles.append(last_element)
        cycles.append(last_element + int(command[1]))

screen = [[]]
for idx, cycle in enumerate(cycles):
    i = int(idx / 40)
    char = '#' if len(screen[i]) >= cycle - 1 and len(screen[i]) <= cycle + 1 else '.'
    screen[i].append(char)
    if len(screen[i]) == 40:
        screen.append([])

def display_screen(screen):
    for row in screen:
        print(''.join(row))

print('PART1', get_required_cycles_sum(cycles, [20, 60, 100, 140, 180, 220]))
print('PART2')
display_screen(screen)