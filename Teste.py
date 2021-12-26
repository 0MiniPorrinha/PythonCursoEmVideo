moeda = str(input('Qual moeda você gostaria de comprar? '))
if(moeda == "Real" ):
    print('Quantidade da compra: ')
    Real = float(input('moeda R$'))
    Dolar = Real / 5.61
    Euro = Real / 6.33
    print('R${:.2f} custa US${:.2f}'.format(Real, Dolar))
    print('R${:.2f} custa €{:.2f}'.format(Real, Euro))
elif(moeda == 'Dolar' ):
    print('Quantidade da compra: ')
    Dolar = float(input('moeda U$'))
    Real = Dolar / 0.18
    Euro = Dolar / 1.13
    print('U${:.2f} custa R${:.2f}'.format(Dolar, Real))
    print('U${:.2f} custa €{:.2f}'.format(Dolar, Euro))
elif(moeda == 'Euro' ):
    print('Quantidade da compra: ')
    Euro = float(input('moeda €'))
    Real = Euro / 0.16
    Dolar = Euro / 0.89
    print('€{:.2f} custa R${:.2f}'.format(Euro, Real))
    print('€{:.2f} custa U${:.2f}'.format(Euro, Dolar))
else:
    print('Moeda inválida')
