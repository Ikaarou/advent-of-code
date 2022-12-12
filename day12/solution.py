#!/usr/bin/env python3
from functools import reduce

file = open('input.txt',mode='r')
lines = file.read().splitlines()

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.parent = None
        self.up = None
        self.left = None
        self.right = None
        self.down = None

    def __repr__(self):
        return 'Node ' + str(self.value) + ' [' + str(self.x) + ',' + str(self.y) + ']'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def node_accessible(self, node, include_s):
        if node is None:
            return False
        if self.value != 'z' and node.value == "E":
            return False
        if self.value == 'S' and include_s is True:
            return True
        if node.value == 'S':
            return False
        if ord(node.value) - ord(self.value) <= 1 or node.value == 'E':
            return True
        return False

    def close_nodes(self, include_s):
        n = []
        if (self.node_accessible(self.right, include_s)):
            n.append(self.right)
        if (self.node_accessible(self.down, include_s)):
            n.append(self.down)
        if (self.node_accessible(self.up, include_s)):
            n.append(self.up)
        if (self.node_accessible(self.left, include_s)):
            n.append(self.left)
        n.sort(key=lambda x: ord(x.value))
        return n

def generate_map():
    map = []
    for x, line in enumerate(lines):
        map.append([])
        for y, node in enumerate(line):
            map[x].append(Node(x, y, node))

    for x, row in enumerate(map):
        for y, node in enumerate(row):
            if node.value == 'S':
                start_node = node
            if x != 0:
                node.up = map[x - 1][y]
            if x != len(lines) - 1:
                node.down = map[x + 1][y]
            if y != 0:
                node.left = map[x][y - 1]
            if y != len(line) - 1:
                node.right = map[x][y + 1]
    return map

def solve(start_node):
    map = generate_map()
    checked = []
    queue  = []
    for row in map:
        for node in row:
            if node.value == start_node:
                queue.append(node)
                checked.append(node)
    step = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        checked.append(current_node)
        if current_node.value == 'E':
            break
        new_nodes = current_node.close_nodes(start_node == 'S')
        for node in new_nodes:
            if node not in queue and node not in checked:
                node.parent = current_node
                queue.append(node)
        step += 1

    path = 0
    while current_node.parent is not None:
        path += 1
        current_node = current_node.parent
    return path

print('Part 1', solve('S'))
print('Part 2', solve('a'))