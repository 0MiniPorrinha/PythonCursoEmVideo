v = int(input('Qual a velocidade? '))

if v > 80:
    multa = (v - 80) * 7
    print('Valor da multa: {}'.format(multa))
else:
    print('Está tudo ok')
