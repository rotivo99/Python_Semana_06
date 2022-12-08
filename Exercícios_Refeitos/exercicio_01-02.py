#!/usr/bin/env python3

#Printing to STDOUT
with open('Python_06.txt', 'r') as song_read: #Abrindo o arquivo
    for line in song_read: #Para cada linha nesse arquivo
        print(line.rstrip().upper()) #Colocar em letra maiúscula e imprimir na tela tirando os espaços extras adicionados automaticamente

print('')

#Printing to new file
with open('Python_06.txt', 'r') as song_read, open('Python_06_uc.txt', 'w') as song_write: #Abrindo o arquivo que será modificado e aquele em que a gente vai salvar as alterações
    for line in song_read: #Para cada linha no arquivo
        song_write.write(line.upper()) #Escrever ela inteira em letra maiúscula - nesse caso, não precisa acrescentar o rstrip()
print('File \'Python_06_uc.txt\' was created') #Aviso ao usuário de que um novo arquivo foi criado
