import math

h = float(input('Digiter a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = l * h
print('A area da parede é {}m²  com {}x{}'.format(area, h, l))

tinta = area / 2
print('E será necessario de {}L de tinta ou {}L arredondando'.format(tinta, math.ceil(tinta)))