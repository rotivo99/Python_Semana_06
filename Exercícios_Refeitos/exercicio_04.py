#!/usr/bin/env python3

line_count = 0 #Criando uma variável para o número de linhas
total_chr_count = 0 #Criando uma variável para o número de caracteres

with open('Python_06.fastq', 'r') as seq_read: #Abrindo o arquivo
    for line in seq_read: #Para cada linha no arquivo de entrada
        line_count += 1 #Acrescentar 1 à variável line_count
        chr_count = len(line) #Variável que conta a quantidade de caracteres na linha
        total_chr_count += chr_count #O valor de chr_count é acrescentado ao total_chr_count a cada iteração para contar o número de caracteres total do arquivo

print(f'The total number of lines in this file is {line_count} and the total number of characters is {total_chr_count}, meaning the average line length is {total_chr_count/line_count}.') #Saída resumindo os dados obtidos
