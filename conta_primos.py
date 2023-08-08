def ePrimo (x):
    i = 1
    tot = 0
    while i <= x:
        if x % i == 0:
            tot += 1
        i += 1
    
    if tot == 2:
        return True
    else: 
        return False
    


def n_primos(n):
    soma_primo = 0
    if n >= 2:
        while n >= 2:
            if ePrimo(n) == True:
                soma_primo += 1
            n -= 1
        
        return soma_primo
        


