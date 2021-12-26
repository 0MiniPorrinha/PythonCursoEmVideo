km = int(input('Digite quantos quilometros a viagem terá: '))
preco = 0
if km <= 200:
    preco = km * 0.50
    print('Custará: {}'.format(preco))
else:
    preco = km * 0.45
    print('Custará: {}'.format(preco))
