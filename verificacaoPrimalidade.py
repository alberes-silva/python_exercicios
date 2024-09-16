
numero = int(input('Digite um numero: '))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print(f'O número {numero}, É PRIMO')
else:
    print(f'O número {numero}, NÃO É PRIMO')