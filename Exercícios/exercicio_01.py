#!/usr/bin/env python3

with open('Anführungszeichen.txt', 'r') as anf_read, open('Python_06_uc.txt', 'w') as anf_write:
    for line in anf_read:
        anf_write.write(line.upper())
print('File \'Python_06_uc.txt\' was created.')
