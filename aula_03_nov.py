#!/usr/bin/env python3

seq_fqo = open('Anführungszeichen_aula.txt', 'w') #Criando um arquivo de texto para escrever o output

with open('Anführungszeichen.txt', 'r') as seq_fh: #Abrindo o arquivo de texto para modificar
    for line in seq_fh: #Para cada linha
        line = line.rstrip().upper() #Vai pegar a linha e colocar em letra maiúscula e armazenar ela na variável line - o strip é para retirar a nova linha que é criada automaticamente
        seq_fqo.write(f'{line}\n') #Vai imprimir a variável line no arquivo novo
