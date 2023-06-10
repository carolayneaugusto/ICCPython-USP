num = int(input('Digite um número inteiro: '))

anterior = num % 10
adjacente = False

while num != 0 and not adjacente:
    numero_res = num // 10
    atual = numero_res % 10
    num = numero_res

    if anterior == atual:
        adjacente = True
    else:
        anterior = atual 

if adjacente: 
    print('sim')
else:
    print('não')
    