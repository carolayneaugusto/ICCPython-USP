def e_hipotenusa(h):
    a = 1
    while a <= h:
        b = 1
        while b <= h:
            if (h**2 == a ** 2 + b ** 2):
                return True
            b += 1
        a += 1
    
    return False

def soma_hipotenusas(n):
    i = 1
    soma = 0
    while i <= n:
        if e_hipotenusa(i) == True:
            soma += i
        i += 1
    return soma


soma_hipotenusas(6)