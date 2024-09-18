texto = input('Digite uma frase: ')
letra = input('Qual letra deseja contar: ')

cont = 0
for i in texto:  # Percorre cada letra no texto
    if i == letra:  # Compara se a letra atual é a que você quer contar
        cont += 1  # Incrementa o contador em 1
print(cont)
