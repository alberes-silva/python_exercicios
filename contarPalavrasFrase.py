texto = input("Digite uma frase aqui: ")

contador = 0

for x in texto.split():
  contador += 1

print("A quantidade de {}".format(contador))
