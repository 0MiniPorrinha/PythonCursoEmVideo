import random
nome = []

for i in range(4):
    lista= input('Digite o nome do aluno: ')
    nome.append(lista)

random.shuffle(nome)
print('A ordem será: ')
print(nome)