from datetime import date

nasc = int(input('Em que ano vc nasceu '))
idade = date.today().year - nasc
print('{} anos'.format(idade))

if idade <= 9:
    print('Nadador Mirim')
elif idade <= 14:
    print('Nadador Infantil')
elif idade <= 19:
    print('Nadador Junior')
elif idade <= 25:
    print('Nadador Senior')
else:
    print('Master')