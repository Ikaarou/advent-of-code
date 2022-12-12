#!/usr/bin/env python3
file = open('input.txt',mode='r')
lines = file.read().splitlines()

temperatures = list(map(lambda t: int(t), lines))
part_1_count = 0
part_2_count = 0
for idx, temp in enumerate(temperatures):
    if (temp > temperatures[idx - 1]):
        part_1_count += 1
    if sum(temperatures[idx:idx+3]) < sum(temperatures[idx+1:idx+4]):
        part_2_count += 1

print('Part1 :', part_1_count)
print('Part2 :', part_2_count)