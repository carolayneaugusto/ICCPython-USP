def maximo(a, b, c):
    maior = a
    if b >= a and b >= c:
         maior = b
    elif c >= a and c >= b:
         maior = c
    else: 
         maior = a
    
    return maior
