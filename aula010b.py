n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2 
print('A sua media foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! parabens!')
else:
    print('Sua média foi ruim!')

## forma simplifiacda
print('PARABENS!' if m >=6 else 'Estude mais!')