peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)
print('imc = {:.2F}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepedo')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')