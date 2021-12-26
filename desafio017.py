import math
from math import sqrt, pow

catO = float(input('Digite o cateto oposto: '))
catA = float(input('Digite o cateto adjacente: '))
hip = math.hypot(catA, catO)

print('A hipotenusa vale: {:.2f}'.format(hip))
