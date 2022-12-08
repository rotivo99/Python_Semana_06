#!/usr/bin/env python3

dictionary = {} #Criando uma variável para armazenar os valores do dicionário

with open('fasta_input.fastq', 'r') as input_read: #Abrindo o arquivo que será analisado
    for line in input_read: #Para cada linha nesse arquivo
        line = line.rstrip() #Vamos tirar o espaço adicionado automaticamente a cada iteração tanto na chave quanto no valor atrelado a ela
        if line.startswith('>'): #Se a linha começar com >
            item = line.replace('>', '') #Vamos retirar o >
        else: #Se a linha não começar com >
            dictionary[item] = line #Ela vira um valor no dicionário
print(dictionary) #Imprimindo o dicionário na tela
