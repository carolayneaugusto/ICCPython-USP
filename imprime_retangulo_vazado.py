largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = 0
# Percorrendo as linhas
while altura > i:
    j = 0
    # Percorrendo as colunas
    while largura > j:
        # Verificando se estamos nas bordas verticais e horizontais
        if (i == 0) or (i == altura - 1) or  (j == 0) or (j == largura - 1):
            print('#', end='')
            # Se não estamos nas bordas verticais/horizontais deixar um espaço em branco
        else:
            print(' ', end='')
        j += 1
    # Para pular de linha    
    print()
    i += 1