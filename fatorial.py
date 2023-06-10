numero = int(input('Digite um número natural: '))

n = numero
i = 1
fatorial = 1

while i <= n:
    fatorial = fatorial * numero
    numero -= 1
    i += 1
print(fatorial)