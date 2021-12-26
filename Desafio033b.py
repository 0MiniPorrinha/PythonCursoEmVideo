a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

#menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior é {} e o menor é\033[1;31m {} \033[m'.format(maior, menor))

