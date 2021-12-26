from datetime import date
ano = date.today().year
maior = 0
menor = 0

print('Digite o ano de nascimento de 7 pessoas')
for i in range(0,7):
    num = int(input('{}° Data: '.format(i + 1)))
    if ano - num < 21:
        menor += 1
    else:
        maior += 1
print('Das 7 pessoas {} são maiores de idade e {} menores de idade'.format(maior, menor))
    