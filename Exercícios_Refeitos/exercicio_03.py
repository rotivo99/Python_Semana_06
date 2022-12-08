#!/usr/bin/env python3

with open('Python_06.seq.txt', 'r') as seq_read, open('Separation.txt', 'w') as separation: #Abrindo arquivos de entrada e saída
    for line in seq_read: #Para cada linha no arquivo de entrada
        new_line = line.split('\t') #Dividir a linha onde tiver tab
        separation.write(f'{new_line[0]}\n{new_line[1]}') #E salvar a lista no arquivo de saída, cada item em uma nova linha

with open('Separation.txt', 'r') as edit, open('Python_06.seq.fasta', 'w') as seq_write: #Abrindo arquivos de entrada e saída
    for line in edit: #Para cada linha no arquivo de entrada
        if line.startswith('c'): #Se a linha começar com c (todas as linhas que não eram sequência comaçavam com c)
            seq_write.write(f'>{line}_reverse_complement\n') #Pegar essa linha e colocar um '>' na frente e um _reverse_complement atrás
        else: #As que não começarem com c, ou seja, forem sequência
            seq_write.write(line.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()) #Vamos trocar tudo pelo nucleotídeo par e colocar em maiúsculo
print('File \'Python_06.seq.fasta\' was created.') #Saída para o usuário saber que um arquivo novo foi gerado
