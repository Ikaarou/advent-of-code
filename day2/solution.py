#!/usr/bin/env python3

file = open('input.txt',mode='r')

points_combinations = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

same_combinations = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

winning_combinations = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

losing_combinations = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

rounds = []
lines = file.read().splitlines()

for line in lines:
    round= line.split(' ')
    rounds.append(round)

total =0

for round in rounds:
    opponenent = round[0]
    player = round[1]
    if player == winning_combinations[opponenent]:
        total += 6
    elif player == same_combinations[opponenent]:
        total += 3

    total += points_combinations[player]




optimal_total = 0
for round in rounds:
    opponnent = round[0]
    player = round[1]
    if player == 'X':
        optimal_total += points_combinations[losing_combinations[opponnent]]
    elif player == 'Y':
        optimal_total += points_combinations[same_combinations[opponnent]] + 3
    else:
        optimal_total += points_combinations[winning_combinations[opponnent]] + 6




print('Total', total)
print('Optimal', optimal_total)