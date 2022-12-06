#!/usr/bin/env python3

file = open('input.txt',mode='r')
file_content = file.read()

START_OF_PACKET_MARKER = 4
START_OF_MESSAGE_MARKER = 14

def all_different(array):
    return len(set(array)) == len(array)

def index_of_different_characters_sequence(content, sequence_length):
    sequence = []
    index = 0
    for char in content:
        if all_different(sequence) and len(sequence) == sequence_length:
            break
        if (len(sequence) == sequence_length):
            sequence.pop(0)
        sequence.append(char)
        index += 1

    return index

print('Part 1', index_of_different_characters_sequence(file_content, START_OF_PACKET_MARKER))
print('Part 2', index_of_different_characters_sequence(file_content, START_OF_MESSAGE_MARKER))

