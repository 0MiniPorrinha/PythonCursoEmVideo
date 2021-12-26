'''frase = str(input('Digite uma frase: ')).lower()
fraseInversa = frase[::-1]
print('Frase escrita: {}'.format(frase))
print('Frase escrita ao contrário: {}'.format(fraseInversa))

if frase.replace(' ', '') == fraseInversa.replace(' ', ''):
    print('"{}" é um Palíndromo'.format(frase))
else:
    print('"{}" não é um Palíndromo'.format(frase))'''


#Com for pq eu sou burro e esqueci
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('"{}" é um Palíndromo'.format(junto))
else:
    print('"{}" não é um Palíndromo'.format(junto))