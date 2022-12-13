#!/usr/bin/env python3
import re
from functools import cmp_to_key

file = open('input.txt',mode='r')
lines = file.read().splitlines()

packets = []
packets_by_two = [[]]
i = 0
for line in lines:
    if line != '':
        p = eval(line)
        packets.append(p)
        packets_by_two[i].append(p)
    else:
        i += 1
        packets_by_two.append([])

def in_right_order(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 == p2:
            return 0
        elif p1 > p2:
            return 1
        else:
            return -1
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i < len(p1) and i < len(p2):
            order = in_right_order(p1[i], p2[i])
            if order == 1:
                return 1
            elif order == -1:
                return -1
            i += 1
        if len(p1) < len(p2):
            return -1
        if len(p1) > len(p2):
            return 1
        return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return in_right_order([p1], p2)
    else:
        return in_right_order(p1, [p2])

c = 0
for i, (left, right) in enumerate(packets_by_two):
    if in_right_order(left, right) == -1:
        c += (i + 1)

print("Part 1", c)

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(lambda p1,p2: in_right_order(p1,p2)))

c2 = 1
for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        c2 *= (i + 1)

print('Part 2:', c2)


