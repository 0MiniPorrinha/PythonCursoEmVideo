print('Digite 6 numeros: ')
soma = 0
for i in range(1, 7):
    valor = int(input('Digite o {}° valor: '.format(i)))
    if valor % 2 == 0:
        soma += valor
        print(soma)
    '''else:
        s = []
        s.append(valor)'''
        
print('A soma de todos os numeros pares é {}'.format(soma))
#print('Numeros impares descartados: {}'.format(s))

#TENTAR COLOCAR UMA LISTA DE NUMEROS EXCLUIDOS