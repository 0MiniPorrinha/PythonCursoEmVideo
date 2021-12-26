a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

#menor
if a < b:
    if a < c:
        menor = a
    else:
        menor = c
else:
    if b < c:
        menor = b
    else:
        menor = c

#maior
if a > b:
    if a > c:
        maior = a
    else:
        maior = c 
else:
    if b > c:
        maior = b
    else:
        maior = c

print('O maior é {} e o menor é {}'.format(maior, menor))

