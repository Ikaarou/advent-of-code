#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().splitlines()

visible_trees = len(lines) * 2 + len(lines[0]) * 2 - 4

forest = []

for line in lines:
    trees = []
    for tree in line:
        trees.append(int(tree))
    forest.append(trees)

# PART 1

def visible_from_left(forest, i, j):
    return max(forest[i][0:j]) < forest[i][j]


def visible_from_right(forest, i, j):
    return max(forest[i][j + 1:len(forest[i])]) < forest[i][j]

def visible_from_top(forest, i, j):
    trees = []
    for k in range(0, i):
        trees.append(forest[k][j])
    return max(trees) < forest[i][j]

def visible_from_bottom(forest, i, j):
    trees = []
    for k in reversed(range(i + 1, len(forest))):
        trees.append(forest[k][j])
    return max(trees) < forest[i][j]


def tallest_from_side(forest):
    total = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest) - 1):
            if (visible_from_left(forest, i, j)):
                total += 1
            elif (visible_from_right(forest, i, j)):
                total += 1
            elif (visible_from_top(forest, i, j)):
                total += 1
            elif (visible_from_bottom(forest, i, j)):
                total += 1

    return total


# PART 2
def tree_count_from_left(forest, i, j):
    count = 0
    for k in reversed(range(0, j)):
        count += 1
        if (forest[i][j] <= forest[i][k]):
            break
    return count

def tree_count_from_right(forest, i, j):
    count = 0
    for k in range(j + 1, len(forest[i])):
        count += 1
        if (forest[i][j] <= forest[i][k]):
            break
    return count

def tree_count_from_top(forest, i, j):
    count = 0
    for k in reversed(range(0, i)):
        count += 1
        if (forest[i][j] <= forest[k][j]):
            break
    return count


def tree_count_from_bottom(forest, i, j):
    count = 0
    for k in range(i + 1, len(forest)):
        count += 1
        if (forest[i][j] <= forest[k][j]):
            break
    return count


def scenic_score(forest):
    max = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest) - 1):
            tmp_max = 1
            tmp_max *= tree_count_from_left(forest, i, j)
            tmp_max *= tree_count_from_right(forest, i, j)
            tmp_max *= tree_count_from_top(forest, i, j)
            tmp_max *= tree_count_from_bottom(forest, i, j)
            if (tmp_max > max):
                max = tmp_max
    return max

visible_trees += tallest_from_side(forest)

print(visible_trees)
print('Sceninc score', scenic_score(forest))

