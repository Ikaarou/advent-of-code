#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

def parse(line):
    direction, steps = line.split()
    steps = int(steps)
    return [direction, steps]

MOVES = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def move_to_apply(head, tail):
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]
    if abs(delta_x) < 2 and abs(delta_y) < 2:
        return (0, 0)

    if abs(delta_x) == 2 and abs(delta_y) == 2:
        return (delta_x / 2, delta_y / 2)

    return (delta_x / 2, delta_y) if abs(delta_x) == 2 else (delta_x, delta_y / 2)

def move_link(link, move):
    return (link[0] + move[0], link[1] + move[1])

def move_rope(rope, move):
    for idx, link in enumerate(rope):
        if idx == 0:
            rope[idx] = move_link(link, move)
        else:
            rope[idx] = move_link(link, move_to_apply(rope[idx - 1], link))

def visited_by_tails_for_rope(rope):
    visited_by_tail = set()
    directions = map(parse, lines)
    for direction, steps in directions:
        move = MOVES[direction]
        for i in range(0, steps):
            move_rope(rope, move)
            visited_by_tail.add(rope[len(rope) - 1])
    return len(visited_by_tail)

rope_1 = [(0, 0), (0, 0)]
rope_2 = [(0, 0) for i in range(0, 10)]

print("PART 1", visited_by_tails_for_rope(rope_1))
print("PART 2", visited_by_tails_for_rope(rope_2))