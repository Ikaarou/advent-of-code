#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

splitted_sacks = []

def get_total_for_letters(letters):
    total = 0
    for letter in letters:
        if letter.isupper():
            total += ord(letter) - 38
        else:
            total += ord(letter) - 96
    return total

def to_set(string):
    return set(list(string))

def find_common_letter(sack_1, sack_2):
    return to_set(sack_1).intersection(to_set(sack_2)).pop()

for line in lines: 
    middle = int(len(line) / 2)
    end = len(line)
    sacks = [line[0:middle], line[middle:end]]
    splitted_sacks.append(sacks)

letters = []
for sacks in splitted_sacks:
    letter = find_common_letter(sacks[0], sacks[1])
    if letter is not None:
        letters.append(letter)

groups = []
i = 0
for group in range(0, int(len(lines) / 3)):
    groups.append(lines[i:i+3])
    i = i+3

badges = []
for group in groups:
    badge = to_set(group[0]).intersection(to_set(group[1]), to_set(group[2])).pop()
    badges.append(badge)

print('Total', get_total_for_letters(letters))
print('Bagdes total', get_total_for_letters(badges))


