#!/usr/bin/env python3

seqs = {}

with open('seq_ex_5.fasta', 'r') as seqs_fh:
    for line in seqs_fh:
        line = line.rstrip()
        if line.startswith('>'):
            seq_id = line
        else:
            print(f'{seq_id} \t {line}')
