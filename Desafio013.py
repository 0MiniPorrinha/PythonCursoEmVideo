salario = float(input('Digite o seu salario: '))
porcentagem = int(input('Digite a porcentagem do aumento: '))
aumento = salario + (salario * porcentagem / 100)
print('Com o seu salario de {} e o aumento de {}% o seu novo salario será {}'.format(salario, porcentagem, aumento))
