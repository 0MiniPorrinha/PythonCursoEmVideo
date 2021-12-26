

num1 = int(input('Digite o valor do lado a: '))
num2 = int(input('Digite o valor do lado b: '))
num3 = int(input('Digite o valor do lado c: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('Os seguimentos podem fazer um triangulo:', end=' ')
    if num1 == num2 == num3:
        print('EQUILATERO')
    elif num1 != num2 != num3 != num1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Não é possivel formar um triangulo')
    

