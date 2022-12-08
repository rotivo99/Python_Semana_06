#!/usr/bin/env python3

genes = {}

with open("sequence_data.txt","r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        gene_id,seq = line.split()
        genes[gene_id] = seq
print(genes)
