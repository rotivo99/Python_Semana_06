#!/usr/bin/env python3

dictionary = {}

with open('Python_06.seq.txt', 'r') as seq_read:
    for line in seq_read:
        line = line.split('\t')
        for nt in line:
            nt_0 = line[0]
            nt_1 = line[0] + '_nucA'
            dictionary[nt_1] = line[1].upper().count('A')
            nt_2 = line[0] + '_nucT'
            dictionary[nt_2] = line[1].upper().count('T')
            nt_3 = line[0] + '_nucC'
            dictionary[nt_3] = line[1].upper().count('C')
            nt_4 = line[0] + '_nucG'
            dictionary[nt_4] = line[1].upper().count('G')
        print(f'In {nt_0}, there are {dictionary[nt_1]} adenines, {dictionary[nt_2]} thymines, {dictionary[nt_3]} citosines and {dictionary[nt_4]} guanines. Its GC content equals to {((dictionary[nt_3]+dictionary[nt_4])/(dictionary[nt_1]+dictionary[nt_2]+dictionary[nt_3]+dictionary[nt_4]))*100}%.')
