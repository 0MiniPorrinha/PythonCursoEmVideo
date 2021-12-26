valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite o prazo (em anos) que pretender pagar: '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar um casa de R${:.2f} em {} anos'.format(valor, anos), end= ' ')
print('A prestação será de {:.2f}'.format(prestacao))

if prestacao >= minimo:
    print('Emprestimo')
else:
    print('É possivel fazer a compra')
