#!/usr/bin/env python3
file = open('input.txt',mode='r')
lines = file.read().splitlines()

epsilon = 0
gamma = 0

gamma_str = ''
epsilon_str = ''
for y in range(len(lines[0])):
    one = 0
    zero = 0
    for x in range(len(lines)):
        if lines[x][y] == '0':
            zero += 1
        else:
            one += 1
    gamma_str += ('0' if zero > one else '1')
    epsilon_str += ('1' if zero > one else '0')
gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)

print('Part 1:', epsilon * gamma)


def compute(keep_lower):
    keep = list(lines)
    for y in range(len(lines[0])):
        zeroes = []
        ones = []
        if len(keep) == 1:
            break
        for x in range(len(keep)):
            if keep[x][y] == '0':
                zeroes.append(keep[x])
            else:
                ones.append(keep[x])
    
        if keep_lower:
            keep = (zeroes if len(zeroes) <= len(ones) else ones)
        else:
            keep = (zeroes if len(zeroes) > len(ones) else ones)
    return int(keep[0], 2)

ogr = compute(keep_lower=False)
csr = compute(keep_lower=True)

print('Part 2', csr * ogr)