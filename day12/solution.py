#!/usr/bin/env python3
from collections import deque 

file = open('input.txt',mode='r')
lines = file.read().splitlines()

def node_accessible(node, target_node, include_s):
    if target_node is None:
        return False
    if node.value != 'z' and target_node.value == "E":
        return False
    if node.value == 'S' and include_s is True:
        return True
    if target_node.value == 'S':
        return False
    if ord(target_node.value) - ord(node.value) <= 1 or target_node.value == 'E':
        return True
    return False

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.parent = None
        self.checked = False
        self.neighbors = []

    def __repr__(self):
        return 'Node ' + str(self.value) + ' [' + str(self.x) + ',' + str(self.y) + ']'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add_neighbors(self, neighbors, include_s):
        n = []
        for node in neighbors:
            if node_accessible(self, node, include_s):
                n.append(node)
        n.sort(key=lambda x: ord(x.value))
        self.neighbors = n
        return self

def generate_map(include_s):
    map = []
    for x, line in enumerate(lines):
        map.append([])
        for y, node in enumerate(line):
            map[x].append(Node(x, y, node))

    for x, row in enumerate(map):
        for y, node in enumerate(row):
            if node.value == 'S':
                start_node = node
            neighbors = []
            if x != 0:
                neighbors.append(map[x - 1][y])
            if x != len(lines) - 1:
                neighbors.append(map[x + 1][y])
            if y != 0:
                neighbors.append(map[x][y - 1])
            if y != len(line) - 1:
                neighbors.append(map[x][y + 1])
            node.add_neighbors(neighbors, include_s)
    return map

def solve(start_node):
    map = generate_map(start_node == 'S')
    queue = deque()
    for row in map:
        for node in row:
            if node.value == start_node:
                queue.append(node)
                node.checked = True
    while len(queue) > 0:
        current_node = queue.popleft()
        current_node.checked = True
        if current_node.value == 'E':
            break
        for node in current_node.neighbors:
            if node not in queue and node.checked is False:
                node.parent = current_node
                queue.append(node)
    path = 0
    while current_node.parent is not None:
        path += 1
        current_node = current_node.parent
    return path

print('Part 1', solve('S'))
print('Part 2', solve('a'))