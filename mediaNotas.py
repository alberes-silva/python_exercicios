
soma_notas = 0
quantidade_notas = 0

while True:

    nota = float(input("Digite uma nota (Para saber a média, digite um número negativo): "))

    if nota < 0:
      break

    soma_notas += nota
    quantidade_notas += 1

if quantidade_notas > 0:

    media = soma_notas / quantidade_notas
    print("A média das notas inseridas é: {}".format(media))
else:
    print("Nenhuma nota válida foi inserida.")





