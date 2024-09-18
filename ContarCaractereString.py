texto = input('Digite uma frase: ')
letra = input('Qual letra deseja contar: ')

cont = 0
for i in texto:
    if i == letra:
        cont += 1
print(cont)
