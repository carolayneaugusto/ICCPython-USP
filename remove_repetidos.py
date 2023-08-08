def remove_repetidos(lista):
    numeros = []

    for x in lista:
        if x not in numeros:
            numeros.append(x)

    return sorted(numeros)

