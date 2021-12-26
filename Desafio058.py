from random import randint

rand = randint(1, 10)
jogada = -1
i = 0

while rand != jogada:
    jogada = int(input('Tente adivinhar um numero de 0 a 10: '))
    if rand == jogada:
        print('Parabens')
    else:
        print('Errou! ')
        i += 1
    print(rand)
    
if i == 0:
    print('Muito bom')
else:
    print('Você venceu, só precisou de {} tentativas'.format(i))