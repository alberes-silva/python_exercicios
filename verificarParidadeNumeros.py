numero_maximo = int(input("Digite um número máximo: "))
contador = 0

for numero in range(1, numero_maximo + 1):
  contador += 1
  if(numero % 2 == 0):
    print(f"O número {contador} é par")
  else:
    print(f"O numero {contador} é impar")