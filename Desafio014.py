unidade = 0
while unidade != 10:
    temperatura = float(input('Digite a temperatura: '))
    print('''1 - Fahrenheit
2 - Celsius
3 - Kelvin
10 sair''')
    unidade = int(input('Digite a unidade  de medida: '))

    if unidade == '1':
        c = (temperatura - 32) / 1.8
        k = (temperatura - 32)*5/9 + 273
        print('Celsius = {}\nKelvin = {}'.format(c, k))
    elif unidade == '2':
        k = temperatura + 273
        f = temperatura * 1.8 + 32
        print('Kelvin = {}\nFahrenheit = {}'.format(k, f))
    elif unidade == '3':
        c = temperatura - 273
        f = ((temperatura - 273) * 1.8) + 32
        print('Celsius = {}\nFahrenheit = {}'.format(c, f))

    else:
        print('Codigo invalido!')