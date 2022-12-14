#!/usr/bin/env python3
import re
from functools import cmp_to_key

SAND_OPENING = (500, 0)

file = open('input.txt',mode='r')
lines = file.read().splitlines()

def display_cave(cave):
    for row in cave:
        print(row)

def get_direction(x1, x2):
    if x1 - x2 == 0:
        return 0
    if x1 - x2 > 0:
        return -1
    return 1

def create_map(input):
    rocks_y = []
    rocks = []

    for line in lines:
        steps = line.split(' ->')
        rock = []
        for step in steps:
            x, y = step.split(',')
            rocks_y.append(int(y))
            rock.append((int(x), int(y)))
        rocks.append(rock)

    cave_y = max(rocks_y)

    cave = [ [] for _ in range(cave_y + 1) ]
    for idx, _row in enumerate(cave):
        cave[idx] = [ '.' for _ in range(1000)]

    cave[SAND_OPENING[1]][SAND_OPENING[0]] = '+'

    for rock in rocks:
        for idx, step in enumerate(rock[1:]):
            previous = rock[idx]
            x_direction = get_direction(previous[0], step[0])
            y_direction = get_direction(previous[1], step[1])
            x = previous[0]
            y = previous[1]
            for _ in range(abs(previous[1] -  step[1]) + 1):
                for _ in range(abs(previous[0]- step[0]) + 1):
                    cave[y][x] = '#'
                    x += x_direction
                y += y_direction

    return cave

def sand_can_move(sand):
    if sand[0] < 0 or sand[0] > len(cave[0]):
        return (-1, -1)
    if sand[1] == len(cave) - 1:
        return (-1, -1)
    if cave[sand[1] + 1][sand[0]] == '.':
        return (0, 1)
    if cave[sand[1] + 1][sand[0] - 1] == '.':
        return (-1, 1)
    if cave[sand[1] + 1][sand[0] + 1] == '.':
        return (1, 1)
    return (0, 0)

def pour_sand(cave):
    count_sand = 0
    end_reached = False
    while end_reached is False:
        sand = SAND_OPENING
        while True:
            move = sand_can_move(sand)
            if move == (-1, -1):
                end_reached = True
                break
            if move == (0, 0):
                if sand == SAND_OPENING:
                    count_sand += 1
                    end_reached = True
                break
            sand = (sand[0] + move[0], sand[1] + move[1])
        if end_reached is False:
            cave[sand[1]][sand[0]] = 'O'
            count_sand +=1
    return count_sand

cave = create_map(lines)

print('Part 1', pour_sand(cave))

cave = create_map(lines)
cave.append([ '.' for _ in range(1000)])
cave.append([ '#' for _ in range(1000)])
print('Part 2', pour_sand(cave))
