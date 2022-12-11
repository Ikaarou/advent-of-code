#!/usr/bin/env python3
from functools import reduce

file = open('input.txt',mode='r')
lines = file.read().split('Monkey')[1:]

class Monkey:
    def __init__(self, id, items, operation, test, results):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.results = results
        self.inspected = 0

    def __repr__(self):
        return 'Monkey ' + str(self.id) + ': _> ' + str(self.inspected) + ' [' + ''.join(str(x) + ', ' for x in self.items) + ']'

    def transform_value(self, item):
        v1 = int(self.operation[0]) if self.operation[0] != 'old' else item
        v2 = int(self.operation[2]) if self.operation[2] != 'old' else item

        return v1 * v2 if self.operation[1] == '*' else v1 + v2

    def throw_to(self, item):
        return self.results[True] if item % self.test == 0 else self.results[False]

def get_total(monkeys):
    inspected = list(map(lambda m: m.inspected, monkeys))
    inspected.sort(reverse=True)
    return reduce(lambda x, y: x*y, inspected[0:2])

def get_monkeys():
    monkeys=[]
    for line in lines:
        elements = line.splitlines()
        id = int(elements[0][1])
        items = list(map(lambda x: int(x), elements[1][elements[1].index(':')+ 2:].split(', ')))
        operation = elements[2][2:].split(' ')[3:]
        test = int(elements[3].split().pop())
        results = {
            True: int(elements[4].split().pop()),
            False: int(elements[5].split().pop()),
        }
        monkeys.append(Monkey(id, items, operation, test, results))
    return monkeys


def part1():
    monkeys = get_monkeys()
    for round in range(20):
        for monkey in monkeys:
            items_to_remove = []
            for idx, item in enumerate(monkey.items):
                monkey.inspected += 1
                new_item = int(monkey.transform_value(item) / 3)
                other_monkey_id = monkey.throw_to(new_item)
                items_to_remove.append(item)
                monkeys[other_monkey_id].items.append(new_item)
            for i in items_to_remove:
                monkey.items.remove(i)
    print('PART1', get_total(monkeys))


def part2():
    modulo = 1
    monkeys = get_monkeys()
    for m in monkeys:
        modulo *= m.test
    for round in range(10000):
        for monkey in monkeys:
            items_to_remove = []
            for idx, item in enumerate(monkey.items):
                monkey.inspected += 1
                new_item = int(monkey.transform_value(item))
                new_item %= modulo
                other_monkey_id = monkey.throw_to(new_item)
                items_to_remove.append(item)
                monkeys[other_monkey_id].items.append(new_item)
            for i in items_to_remove:
                monkey.items.remove(i)
    print('PART2', get_total(monkeys))


part1()
part2()
