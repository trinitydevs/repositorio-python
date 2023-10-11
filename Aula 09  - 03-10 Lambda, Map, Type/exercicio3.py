def imprimePrimos(n):
  i = 2
  while i <= n:
    if eprimo(i):
      print(i)
    i += 1

def eprimo(n):
  if n <= 1:
    return False
  if n % 2 == 0:
    return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

print("Números primos entre 1 e 500:")
imprimePrimos(500)
