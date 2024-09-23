numeros = [30, 15, -9, -10, 27, 22, 16, 2, -8]

soma_positivos = 0

for numero in numeros:
    if numero > 0:
        soma_positivos += numero

print(f"A soma dos números positivos é: {soma_positivos}")
