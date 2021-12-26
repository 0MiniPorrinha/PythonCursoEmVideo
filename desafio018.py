import math

ang = float(input('Digite um angulo: '))
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno, cosseno e tangente de {} é respectivamnete {:.2f}, {:.2f}, {:.2f}'.format(ang, sin, cos, tan))
