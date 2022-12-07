#!/usr/bin/env python3

file = open('input.txt',mode='r')
lines = file.read().split('$ ')

class Folder:
    def __init__(self):
        self.size = 0
        self.folders = []
        self.name = None
        self.parent = None

    def has(self, name):
        present = False
        for folder in self.folders:
            if folder.name == name:
                present = True
        return present



file_system = Folder()

def get_folders_size(big_folder, size_under, folder_with_enough_space, space_to_free = 0):
    sub_folder_size = 0
    for folder in big_folder.folders:
        size, size_under, folder_with_enough_space = get_folders_size(folder, size_under, folder_with_enough_space, space_to_free)
        sub_folder_size += size
    folder_size = big_folder.size + sub_folder_size
    if folder_size < 100000:
        size_under += folder_size
    if folder_size > space_to_free:
        folder_with_enough_space.append(folder_size)
    return folder_size, size_under, folder_with_enough_space

def add_folder(current_folder, name):
    folder = Folder()
    folder.name = name
    folder.parent = current_folder
    current_folder.folders.append(folder)
    return folder

commands = []
for line in lines:
    command = line.split('\n')
    if len(command) != 1:
        if (command[0][0:2] == 'cd'):
            command = command[0].split(' ')
        commands.append(command)

current_folder = file_system
for command in commands:
    if command[0] == 'cd':
        dirname = command[1]
        if dirname == '..':
            current_folder = current_folder.parent
        elif dirname != '/':
            if current_folder.has(command[1]) == False:
                current_folder = add_folder(current_folder, command[1])
            else:
                current_folder = current_folder.has(command[1])
    elif command[0] == 'ls':
        files = list(filter(lambda file:  'dir ' not in file and file != '', command[1:]))
        size = 0
        for file in files:
            size += int(file.split(' ')[0])
        current_folder.size = size

size, size_under, folder_under = get_folders_size(file_system, 0, [])
print('part 1', size_under)
size, size_under, folder_under = get_folders_size(file_system, 0, [], 30000000 - (70000000 - size))
print('part 2', min(folder_under))




