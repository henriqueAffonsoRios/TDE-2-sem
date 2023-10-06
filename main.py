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

# Calcula o mod

def mod_calc(a, b):
  if a < b:
    return a
  else:
    resto = a % b
    return resto

# Gera um número "E" aleatório, que satisfaz a condição "mdc(totient_N, E) == 1"

def generate_E(totient_N):
  E = random.randrange(1, totient_N)

  while True:
    if(MDC(totient_N, E) == 1):
      return E

# Implementando os valores para a criptografia

p = generate_prime()
q = generate_prime()

N = p * q # Um dos componentes para a criação da chave pública
totient_N = (p-1) * (q-1)

E = generate_E(totient_N) # Segundo componente para a criação da chave pública

public_key = (N, E) # Chave pública gerada para encriptação
