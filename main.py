import math
import random

# Gerando chave pública

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
    num_primo = random.randrange(3, 300)

    if(prime(num_primo) == True):
      return num_primo

# Implementando os valores para chave pública

p = generate_prime()
q = generate_prime()

N = p * q # Um dos componentes para a criação da chave pública
totient_N = (p-1) * (q-1)

# Gera um número "E" aleatório, que satisfaz a condição "mdc(totient_N, E) == 1"

def generate_E(toti):
  E = random.randrange(1, toti)

  while True:
    if(MDC(toti, E) == 1):
      return E

E = generate_E(totient_N) # Segundo componente para a criação da chave pública

public_key = (N, E) # Chave pública gerada para encriptação
print('Esta é sua chave pública ', public_key)

# Gerando chave privada

# Calcula o mod

def mod_calc(a, b):
  if a < b:
    return a
  else:
    resto = a % b
    return resto

# Gera a chave privada

def generate_chave_priv(totient_N, E):
  priv_key = 0

  while(mod_calc(priv_key * E, totient_N) != 1):
    priv_key += 1

  return priv_key

private_key = generate_chave_priv(totient_N, E)
print('Esta é sua chave privada', private_key)

# Criptografa uma mensagem

def encript(msg, N, E):
  tamanho = len(msg)
  msg_encript = []

  for i in range(0, tamanho):
    letra_ascii = ord(msg[i])
    X = letra_ascii ** E
    res = mod_calc(X, N)

    msg_encript.append(res)

  return msg_encript

msg = input("Insira uma mensagem: ")
msg_encript = encript(msg, N, E)

print(*msg_encript, sep="")

# Descriptografa uma mensagem

def decript(msg_encript, N, private_key):
  tamanho = len(msg_encript)
  valores = []

  for i in range(0, tamanho):
    X = msg_encript[i] ** private_key
    res = mod_calc(X, N)
    letra = chr(res)

    valores.append(letra)

  return valores

msg_decript = decript(msg_encript, N, private_key)
print(*msg_decript, sep="")
