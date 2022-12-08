#!/usr/bin/env python3

total_chr_count = 0

with open('Python_06.fastq', 'r') as fastq_read:
    for line in fastq_read:
        number_lines = len(fastq_read.readlines())
        chr_count = len(line)
        total_chr_count += chr_count
print('The total number of lines is:', number_lines)
print('The total character count is:', total_chr_count)
print('The average of characters per line is:', total_chr_count/number_lines)
