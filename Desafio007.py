n = int(input('Digite a quantidade de notas: '))
soma = 0

for i in range(1, n+1):
    valor = int(input('Digite a nota {}: '.format(i)))
    soma += valor
    print(valor)
    print(soma)

media = soma / n
print('A media das {} notas é {}'.format(n, media))