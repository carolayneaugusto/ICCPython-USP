import math

a = float(input('Informe o primeiro parâmetro: '))
b = float(input('Informe o segundo parâmetro: '))
c = float(input('Informe o terceiro parâmentro: '))

delta = (b ** 2) - 4 * a * c
raiz1 = raiz2 =  0

if (delta < 0):
    print('esta equação não possui raízes reais')
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    if delta == 0:
        print(f'a raiz desta equação é {raiz1}')
    else:
        if delta > 0:
            if raiz1 < raiz2:
                print(f'as raízes da equação são {raiz1} e {raiz2}')
            else:
                print(f'as raízes da equação são {raiz2} e {raiz1}')


    
