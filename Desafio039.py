from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
idade = ano - nascimento

if idade < 18:
    saldo = 18 - idade
    print('Ainda falta um tempo para o seu alistamento')
    print('Ainda faltam {} anos'.format(saldo))
    print('O seu alistamento será em {}'.format(ano + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Já passou da hora de se alistar')
    print('Já se passaram {} anos'.format(saldo))
    print('Seu foi em: {}'.format(ano - saldo))
else:
    print('É a hora de se alistar')
