import random

rand = random.randint(1, 5)
n = int(input("Tente advinhar um numero de 1 a 5: "))

if n == rand:
    print('Você acecrtou!')
else:
    print('Você errou :(')
print('o valor é: {}'.format(rand))
    