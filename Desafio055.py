maior = 0
menor = 0

print('Digite o peso de 5 pessoas: ')

for i in range(0,5):
    
    num = float(input('Digite o {}° peso: '.format(i + 1)))
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        
print('menor: {}      maior: {}'.format(menor, maior))