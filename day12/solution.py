    #!/usr/bin/env python3
from collections import deque 

START = 'S'
END = 'E'

file = open('input.txt',mode='r')
lines = file.read().splitlines()

def node_accessible(node, target_node):
    if target_node is not None and ord(target_node.value) - ord(node.value) <= 1:
        return True
    return False

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.depth = 0
        self.visited = False
        self.neighbors = []

    def __repr__(self):
        return 'Node ' + str(self.value) + ' [' + str(self.x) + ',' + str(self.y) + ']'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add_neighbors(self, neighbors):
        n = []
        for node in neighbors:
            if node_accessible(self, node):
                n.append(node)
        n.sort(key=lambda x: ord(x.value))
        self.neighbors = n

def generate_map(start_node):
    map = []
    starts = []
    end = None
    for x, line in enumerate(lines):
        map.append([])
        for y, node in enumerate(line):
            n = Node(x, y, node)
            if node == start_node or node == START:
                n.value = 'a'
                starts.append(n)
            elif node == END:
                n.value = 'z'
                end = n
            map[x].append(n)

    for x, row in enumerate(map):
        for y, node in enumerate(row):
            neighbors = []
            if x != 0:
                neighbors.append(map[x - 1][y])
            if x != len(lines) - 1:
                neighbors.append(map[x + 1][y])
            if y != 0:
                neighbors.append(map[x][y - 1])
            if y != len(line) - 1:
                neighbors.append(map[x][y + 1])
            node.add_neighbors(neighbors)
    return map, starts, end

def solve(start_node):
    map, starts, end = generate_map(start_node)
    queue = deque(starts)
    while len(queue) > 0:
        current_node = queue.popleft()
        current_node.visited = True
        if current_node == end:
            break
        for node in current_node.neighbors:
            if node not in queue and node.visited is False:
                node.depth = current_node.depth + 1
                queue.append(node)
    return current_node.depth

print('Part 1', solve(START))
print('Part 2', solve('a'))