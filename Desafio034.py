salario = float(input('Qual o seu salario? '))

if salario <= 1250:
    print('Com o aumento o salario será de: {}'.format(salario + (salario * 0.15)))
else:
    print('Com o aumento o salario será de: {}'.format(salario + (salario * 0.1)))