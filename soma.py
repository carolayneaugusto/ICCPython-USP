numero = int(input('Digite um número inteiro: '))

n = str(numero)
i = 1
soma = 0
while i <= len(n):
    numero_res = numero // 10
    soma += (numero % 10)
    numero = numero_res
    i += 1
print(soma)
