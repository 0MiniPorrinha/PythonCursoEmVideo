print('Digite os seguintes itens (nome, idade, sexo) de 5 pessoas: ')

media = 0
maior = 0
menor20 = 0

for i in range(0, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: (M/F): '))
    media += idade
    
    if (sexo == 'M' or sexo =='m') and idade > maior:
        maior = idade
        velho = nome
    if (sexo == 'F' or sexo == 'f') and idade < 20:
        menor20 += 1
media = media / 5

print('''A media de idade do grupo é {}
O Homem mais velho é o {}
E tem {} mulheres menores de 20 anos'''.format(media, velho, menor20))