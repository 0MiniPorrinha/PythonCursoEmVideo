c = 1

while c != 0:
    sexo = str(input('Digite o sexo: ')).upper()
    print(sexo)
    if sexo == 'M' or sexo == 'F':
        c = 0
    else:
        print('Digite um valor valido! Digite novamente')
        
print('Cadastrado ')