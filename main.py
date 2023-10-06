import math
import random


msg = "Esta é uma mensagem"

# Declarando a função MDC (Máximo Divisor Comum)

def MDC(a, b):
  while(b != 0):
    r = a % b
    a = b
    b = r
  return a

# Verifica se o número recebido é primo

def prime(num):
  divs = []

  for i in range(1, num + 1):
    if(num % i == 0):
      divs.append(i)

  qtd_divs = len(divs)

  if(qtd_divs > 2):
    return False
  else:
    return True

# Gera um número primo aleatório

def generate_prime():
  while True:
    num_primo = random.randrange(1, 200)

    if(prime(num_primo) == True):
      return num_primo

print(generate_prime())

# Calcula o mod
