num = int(input('Digite um numero inteiro: '))
valor = 0
for i in range(2, num):
    if num % i == 0:
        valor += 1

if valor != 0:
    print('Não é primo')
else:
    print('É primo')
    