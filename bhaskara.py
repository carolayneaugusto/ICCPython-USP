import math

def delta(a, b, c):
    return (b ** 2) - 4 * a * c


def main():
    a = float(input('Informe o primeiro parâmetro: '))
    b = float(input('Informe o segundo parâmetro: '))
    c = float(input('Informe o terceiro parâmentro: '))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):    
    d = delta(a, b, c)

    if (d < 0):
        print('esta equação não possui raízes reais')
    else:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)

        if delta == 0:
            print(f'a raiz desta equação é {raiz1}')
        else:
            if d > 0:
                if raiz1 < raiz2:
                    print(f'as raízes da equação são {raiz1} e {raiz2}')
                else:
                    print(f'as raízes da equação são {raiz2} e {raiz1}')
            else:
                print('Essa equação não tem raízes.')
