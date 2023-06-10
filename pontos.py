import math

x1 = float(input('X1: '))
y1 = float(input('Y1: '))

x2 = float(input('X2: '))
y2 = float(input('Y2: '))

distancia = math.sqrt(((x1 - x2) ** 2 ) + ((y1 - y2) ** 2))

if distancia >= 10:
    print('longe')
else:
    print('perto')
    