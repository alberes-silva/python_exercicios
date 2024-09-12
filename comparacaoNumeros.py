numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

valorMax = max(numero1,numero2, numero3)
valorMin = min(numero1,numero2, numero3)

print(f'valor máximo é {valorMax} e mínimo é {valorMin}')

if numero1 > numero2 > numero3:
    print('Valor decrescente')
elif numero3 > numero2 > numero1:
    print('Valor crescente')
else:
    print( 'Valor não estão ordenados')