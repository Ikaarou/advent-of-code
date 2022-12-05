#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

def get_letters(crates):
    letters = []
    for i in range(1, len(crates) + 1):
        letters.append(crates[i][0])
    return ''.join(letters)

def build_crates(input):
    crates_number = int((len(lines[0]) + 1) / 4)
    crates = {}

    for i in range(1, crates_number + 1):
        crates[i] = []

    for line in input:
        if line.find('[') == -1:
            break
        crates_index = 1
        i = 0
        while(i < len(line)):
            crate = line[i+1]
            if (crate != ' '):
                crates[crates_index].append(crate)
            i += 4
            crates_index += 1
    return crates

def build_actions(input):
    actions = []
    start = 0
    for line in input:
        start += 1
        if line.find('[') == -1:
            break

    for i in range(start + 1, len(input)):
        words = input[i].split(' ')
        actions.append({ 'move': int(words[1]), 'start': int(words[3]), 'end': int(words[5])})
    return actions

def part1():
    crates = build_crates(lines)
    actions = build_actions(lines)
    for action in actions:
        for j in range(0, action['move']):
            crate = crates[action['start']].pop(0)
            crates[action['end']].insert(0, crate)
    return get_letters(crates)

def part2():
    crates = build_crates(lines)
    actions = build_actions(lines)
    for action in actions:
        pile = []
        for j in range(0, action['move']):
            crate = crates[action['start']].pop(0)
            pile.append(crate)

        crates[action['end']] = pile + crates[action['end']]
    return get_letters(crates)


print("1:", part1())
print("2:", part2())

