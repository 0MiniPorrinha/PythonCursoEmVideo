print('Digite dois numeros')
num1 = int(input('Primeiro: '))
num2 = int(input('Segundo: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')