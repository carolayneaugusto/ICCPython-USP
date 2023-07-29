'''
LEr uma sequência de números digitados pelo usuário e, para cada número digitado, informar o seu fatorial
'''

# ler uma sequência de números - while
num = int(input('Informe um número inteiro: '))

while  num >= 0:
    fatorial = 1
    x = num
    while x > 1:
        fatorial = fatorial * x
        x -= 1
    print (f'O fatorial de {num} é: {fatorial}')
    num = int(input('Informe um número inteiro: '))
print('\nFIM')
