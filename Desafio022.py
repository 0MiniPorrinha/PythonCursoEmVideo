nome = str(input('Digite o seu nome completo:')).strip()
dividido = nome.split()
print('Nome maiusculo: {}'.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))
print('Numero de caracteres sem espaço: {}'.format(len(nome) - nome.count(' ')))
print('Numero de caracteres do primeiro nome: {}'.format(len(dividido[0])))
#outro medodo
print('Numero de caracteres do primeiro nome: {}'.format(nome.find(' ')))
