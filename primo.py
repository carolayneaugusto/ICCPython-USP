numero = int(input('Digite um número inteiro: '))

i = 1
total = 0
while i <= numero:
    if numero % i == 0:
        total += 1
    i += 1

if total == 2:
    print('primo')
else:
    print('não primo')
