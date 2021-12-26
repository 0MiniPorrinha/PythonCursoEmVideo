num = int(input('Digite o numero inteiro: '))
print('''Escolha uma das opções para conversão:
[ 1 ] converter BINÁRIO
[ 2 ] converter OCTAL
[ 3 ] converter HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1: 
    print('{} em binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} em OCTAL é {}'. format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em HEXADECIMAL é {}'. format(num, hex(num)[2:]))
else:
    print('Codigo invalido')