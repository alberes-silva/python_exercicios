from math import factorial

#Fatorial usando a biblioteca math
# numero = int(input('Digite um número: '))
# fatorialNumero = factorial(numero)
# print(f'O fatorial de {numero} é {fatorialNumero}')


#Fatorial tradicional
numero = int(input('Digite um número: '))
if numero < 0:
    print('Por favor, digite um número inteiro positivo')
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f'O fatorial de {numero} é igual a {fatorial}')




