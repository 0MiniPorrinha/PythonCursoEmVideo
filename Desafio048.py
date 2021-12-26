soma = 0
cont = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        cont += 1
        soma += i
        print(i)
print('A soma é: {} e foram somados {} numeros'.format(soma, cont))