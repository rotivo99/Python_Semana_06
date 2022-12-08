#!/usr/bin/env python3

print('Maneira 1')
file_object_fullpath = r'/home/rotivo/Python_Semana_06/Tartaruga.txt'

file_object = open(file_object_fullpath, "r")
print(file_object.read())
file_object.close()

print('Maneira 2')
file_object = open("Tartaruga.txt","r")
print(file_object.read())
file_object.close()

print('Maneira 3')
file_object = open("Tartaruga.txt","r")

for line in file_object:
    print(line)

print('Maneira 3 com .rstrip()')
file_object = open("Tartaruga.txt","r")

for line in file_object:
    line = line.rstrip()
    print(line)

print('Maneira 4')
with open("Tartaruga.txt", "r") as file_object:
    print(file_object.read())

print('Maneira 5')
with open('Tartaruga.txt', 'r') as file_object:
    for line in file_object:
        line = line.rstrip()
        print(line)
