preco = float(input('Digite o preço do produto: '))
desconto = int(input('Digite a porcentagem do desconto: '))
valor = preco - (preco * desconto / 100)
print('O produto custa {} mas com {}% de desconto custa {:.2f}'.format(preco, desconto, valor))