#!/usr/bin/env python3
import re

file = open('input.txt',mode='r')
lines = file.read().splitlines()

REQUIRED_ROW = 2000000
MAX_COORDINATE = 4000000

def tuning_frequency(x, y):
    return 4000000 * x + y

def to_int(v):
    return int(re.sub("[^0-9\-]", "", v))

row = set()
sensors = []
for line in lines:
    sx, sy, _, _, _, _, bx, by = line.split()[2:]
    sx, sy, bx, by = to_int(sx), to_int(sy), to_int(bx), to_int(by)
    manhattan = abs(sx - bx) + abs(sy - by)
    sensors.append([sx, sy, manhattan])
    def already_occupied(x):
        if (bx == x and by == REQUIRED_ROW):
            return True
        if (sx == x and sy == REQUIRED_ROW):
            return True
        return False

    for x in range(sx - manhattan, sx + manhattan + 1):
        remaining = abs(abs(sx - x) - manhattan)
        if (sy - remaining <= REQUIRED_ROW <= sy + remaining):
            if not already_occupied(x):
               row.add((x, REQUIRED_ROW))
print('Part 1:', len(row))

def is_distress(x, y):
    for sx, sy, m in sensors:
        m2 = abs(x - sx) + abs(y - sy)
        if m2 <= m:
            return False
    return True

def fetch_distress_beacon():
    for sx, sy, manhattan in sensors:
        for mx in range(manhattan + 2):
            my = (manhattan + 1) - mx
            for move_x, move_y in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                x = sx + (mx * move_x)
                y = sy + (my * move_y)
                if 0 <= x <= MAX_COORDINATE and 0 <= y <= MAX_COORDINATE and is_distress(x, y):
                    return tuning_frequency(x, y)

print("Part 2:", fetch_distress_beacon())
