def fatorial(num):
    x = num
    fatorial = 1
    while x > 1:
        fatorial = fatorial * x
        x -= 1
    print(f'O fatorial de {num} é {fatorial}')


num = int(input('Digite um número inteiro: '))

while num >= 0:
    fatorial(num)
    num = int(input('Digite um número inteiro: '))
print('\nFIM')