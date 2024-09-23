import random

numeros_aleatorios = []

for _ in range(10):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

print("Lista de 10 números aleatórios:", numeros_aleatorios)