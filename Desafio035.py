def verifica(num1, num2, num3):

    if num2 > num3:
        modulo = num2 - num3
    else:
        modulo = num3 - num2

    soma = num2 + num3

    if num1 > modulo and num1 < soma:
        print('Com esses lados é possivel fazer um tiangulo')
    else:
        print('Com esses lados NÃO é possivel fazer um tiangulo')
    
    print('{} < {} < {} \n \n \n'.format(modulo, num1, soma))

a = int(input('Digite o valor do lado a: '))
b = int(input('Digite o valor do lado b: '))
c = int(input('Digite o valor do lado c: '))

print('modulo > lado > soma')
verifica(a, b, c)
verifica(c, a, b)
verifica(b, c, a)

