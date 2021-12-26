frase = str(input('Digite uma frase: ')).strip()

print('Quantidade de A: {}'.format(frase.upper().count('A')))
print('Peimeiro A na posição: {}'.format(frase.upper().find('A') + 1))
print('Ultimo A na posição: {}'.format(frase.upper().rfind('A') + 1))


