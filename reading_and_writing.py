#!/usr/bin/env python3

import re

total_amino = 0 #Criando uma variável zerada para armazenar os valores do for in
line_count = 0 #Criando uma variável zerada para armazenar os valores do for in

with open('protein.txt', 'r') as seq_read, open('amino_output_count.txt', 'w') as seq_write: #Abrindo o arquivo e criando outro para armazenar o output
    for seq in seq_read: #Para cada seq na variável seq_read
        line_count += 1 #Vai pegar o line_count e acrescentar 1 a cada iteração (conta o número de linhas)
        seq = seq.strip()
        amino_count = len(seq) #Atribuindo a quantidade de itens de seq a uma variável
        total_amino += amino_count #A cada iteração, esse valor será acrescentado a total_amino para depois a gente saber o valor de aminoácidos somando todas as sequências
        seq_write.write(f'Line: {line_count} \t Total aminoacid count: {amino_count}\n') #Escrevendo o número da linha e a quantidade de aminoácidos naquela linha em um arquivo novo 
    seq_write.write(f'Total line count: {total_amino}\n') #Escrevendo o número de aminoácidos totais no novo arquivo - tá identado junto com o for, porque a gente só vai ter o número final de aminoácidos quando ele acabar.
print('Output saved as \'amino_output_count.txt\'.') #Uma mensagem avisando o usuário de que o novo arquivo foi gerado, importante para que ele saiba que algo aconteceu
