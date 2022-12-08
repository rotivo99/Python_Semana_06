#!/usr/bin/env python3

with open('Xanthomonas_citri_23S.txt', 'r') as seq_read, open('Xanthomonas_citri_23S_lowercase', 'w') as seq_write:
    for line in seq_read:
        seq_write.write(line.lower())
print('File \'Xanthomonas_citri_23S_lowercase\' was generated.')

with open('Xanthomonas_citri_23S.txt', 'r') as seq_read, open('Xanthomonas_citri_23S_reverse', 'w') as seq_write:
    for line in seq_read:
        seq_write.write(line)
        replacement1 = seq_write.write(line.replace('A', 't'))
        replacement2 = seq_write.write(str(replacement1).replace('T', 'a'))
        replacement3 = seq_write.write(str(replacement2).replace('G', 'c'))
        replacement4 = seq_write.write(str(replacement3).replace('C', 'g'))
        seq_write.write(str(replacement4).upper())
print('File \'Xanthomonas_citri_23S_reverse\' was generated.')
