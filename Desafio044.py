preco = float(input('Qual o valor do produto?'))
print('Qual a opção de pagamento? ')
opcao = int(input('''1 - À vista no dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão\n'''))

if opcao == 1:
    total = preco - preco * 10 / 100
    print('A vista no dinheiro/cheque fica com 10% de desconto: R${}'.format(total))
elif opcao == 2:
    total = preco - preco * 5 / 100
    print('A vista no cartão fica com 5% de desconto: R${}'.format(total))
elif opcao == 3:
    total = preco
    print('Em até 2x no cartão fica com o preço normal: R${}'.format(total))
    parcela = preco / 2
    print('E cada parcela será de {}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelatotal = int(input('Quantas parceclas? '))
    parcela = total / parcelatotal
    print('Em {}x no cartão fica com 20% de juros: R${}'.format(parcelatotal, total))
    print('E cada parcela será de: {}'.format(parcela))
else:
    print('Codigo invalido')