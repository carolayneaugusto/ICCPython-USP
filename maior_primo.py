def ePrimo(k):
  i = 1
  tot = 0

  while i <= k:
    if k % i == 0:
      tot += 1
    i += 1

  if tot == 2:
    primo = True
  else:
    primo = False
  
  return primo



def maior_primo(n):
  while n > 0:
    if ePrimo(n) == True:
      return n
    else:
        n -= 1

    