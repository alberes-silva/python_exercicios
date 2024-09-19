
texto = input('Digite a palavra que deseja ser invertida: ')

invertido = ''

for i in range(len(texto)-1, -1, -1):
    invertido += texto[i]
print(f"A palavra invertida é: {invertido}")
