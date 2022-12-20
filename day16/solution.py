#!/usr/bin/env python3
import re

file = open('input.txt',mode='r')
lines = file.read().splitlines()

TIME = 30
MOVE_COST = 1
OPENING_COST = 1

def to_int(v):
    return int(re.sub("[^0-9\-]", "", v))

def to_name(v):
    return re.sub("[^A-Z]", "", v)

class Valve:
    def __init__(self, name, pressure, tunnels_keys):
        self.name = name
        self.pressure = pressure
        self.tunnels_keys = tunnels_keys
        self.distances = {}
        self.tunnels = []

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash((self.name, self.pressure))

    def __repr__(self):
        return 'Valve ' + self.name + ': ' + str(self.pressure)

valves = []
for line in lines:
    name = line.split()[1]
    pressure = to_int(line.split()[4])
    tunnels_keys = list(map(lambda v: to_name(v), line.split()[9:]))
    v = Valve(name, pressure, tunnels_keys)
    valves.append(v)

for v in valves:
    for t_key in v.tunnels_keys:
        v.tunnels.append([x for x in valves if x.name == t_key][0])

def find_depth(valves, target):
    depth = 1
    queue = set(valves)
    while True:
        next_frontier = set()
        for x in queue:
            if x == target:
                return depth
            for y in x.tunnels:
                next_frontier.add(y)
        queue = next_frontier
        depth += MOVE_COST
    return depth

def fill_distances():
    for current in valves:
        current.distances = {}
        for target in valves:
            if current.name != target.name:
                current.distances[target.name] = find_depth(current.tunnels, target)
            else:
                current.distances[target.name] = 0

fill_distances()

def find_valve(valves, name):
    for v in valves:
        if v.name == name:
            return v
    return None

cache = {}

def cache_key(current_pressure, current_room, remaining_time, open_valves):
    return current_room.name + ''.join([v.name for v in open_valves])+str(current_pressure)+str(remaining_time)

def max_flow(current_pressure, current_room, remaining_time, open_valves):
    key = cache_key(current_pressure, current_room, remaining_time, open_valves)
    if key in cache:
        return cache[key]
    if remaining_time <= 0 or len(open_valves) == 0:
        return current_pressure
    if current_room in open_valves and current_room.pressure != 0:
        remaining_valves = [v for v in open_valves if v.name != current_room.name]
        return max_flow(current_pressure + current_room.pressure * remaining_time, current_room, remaining_time - OPENING_COST, remaining_valves)
    else:
        potential_pressures = []
        for open_valve in open_valves:
            potential_pressures.append(max_flow(current_pressure, open_valve, remaining_time - current_room.distances[open_valve.name], open_valves))
    best_pressure = max(potential_pressures)
    cache[key] = best_pressure
    return best_pressure

def part1(valves):
    first_valve = find_valve(valves, 'AA')
    valves = list(filter(lambda v: v.pressure > 0, valves))
    return max_flow(0, first_valve, TIME - 1 if first_valve.pressure == 0 else 0, valves) # minus one is needed because we start on 0 pressure event




def part2(valves):
    first_valve = find_valve(valves, 'AA')
    valves = list(filter(lambda v: v.pressure > 0, valves))

    MAX = 0

    def max_flow_with_elephant(current_room, remaining_time, open_valves):
        nonlocal MAX
        best = max_flow(0, current_room, 25, open_valves)
        for open_valve in open_valves:
            remaining_valves = [v for v in open_valves if v.name != open_valve.name]
            result = open_valve.pressure * (remaining_time - open_valve.distances[current_room.name]) + max_flow_with_elephant(open_valve, remaining_time - current_room.distances[open_valve.name] - 1 , remaining_valves)
            if result > best:
                best = result
            if result > MAX:
                print(result)
                MAX = result
        return best

    return max_flow_with_elephant(first_valve, 25, valves)

print('Part 1:', part1(valves))
print("Part 2:", part2(valves))
