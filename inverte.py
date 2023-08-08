lista = []
n = int(input('Digite um número: '))

while n != 0:
    lista.append(n)
    n = int(input('Digite um número: '))

lista.reverse()
for num in lista:
    print(num)

