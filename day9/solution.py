#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

MOVES = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def should_move_tail(head, tail):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return True
    return False

def should_follow(head, link):
    return abs(head[0] - link[0]) + abs(head[1] - link[1]) < 3 and (abs(head[1] - link[1]) > 0 and abs(head[0] - link[0]) >0)

def increment_value(x1, x2):
    if (x1 - x2) > 0:
        return 1
    if (x1 - x2) < 0:
        return -1
    return 0

def is_tail(rope, idx):
    return idx == len(rope) - 2

def move_rope(rope, old_head_position, visited_by_tail):
    for idx, link in enumerate(rope[1:]):
        if (should_move_tail(rope[idx], link)):
            if should_follow(rope[idx], link):
                rope[idx + 1] = old_head_position
                old_head_position = link
            else:
                new_link = (link[0] + (increment_value(rope[idx][0], link[0])), link[1] + (increment_value(rope[idx][1], link[1])))
                rope[idx + 1] = new_link
                old_head_position = new_link

            if (is_tail(rope, idx)):
                visited_by_tail.append(rope[idx + 1])
        else:
            break

def visited_by_tails_for_rope(rope):
    visited_by_tail = [(0, 0)]
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        move = MOVES[direction]
        for i in range(0, steps):
            old_head = rope[0]
            rope[0] = (old_head[0] + move[0], old_head[1] + move[1])
            move_rope(rope, old_head, visited_by_tail)
    return len(list(set(visited_by_tail)))


rope_1 = [(0, 0), (0, 0)]

rope_2 = []
for i in range(0, 10):
    rope_2.append((0, 0))

print("PART 1", visited_by_tails_for_rope(rope_1))
print("PART 2", visited_by_tails_for_rope(rope_2))