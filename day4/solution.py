#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

groups = []
for line in lines:
    elves = line.split(',')
    groups.append([set([]), set([])])
    for id, elve in enumerate(elves):
        start = int(elve.split('-')[0])
        end = int(elve.split('-')[1]) + 1
        for i in range(start, end):
            groups[len(groups) - 1][id].add(i)

fully_intersected = 0
for group in groups:
    e_1 = group[0]
    e_2 = group[1]
    intersection_len = len(e_1.intersection(e_2))
    if intersection_len == len(e_2) or intersection_len == len(e_1):
       fully_intersected += 1

intersect_once = 0
for group in groups:
    e_1 = group[0]
    e_2 = group[1]
    if len(e_1.intersection(e_2)) > 0 :
       intersect_once += 1

print(len(groups))
print('Groups fully contained in other', fully_intersected)
print('Groups overlapping once', intersect_once)