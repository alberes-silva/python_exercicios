numero = int(input("Digite um número (inteiro): "))

if numero % 2 == 0 and numero > 0:
    print(f'O número {numero} é par e positivo')
elif numero % 2 == 0 and numero < 0:
    print(f'O número {numero} é par e negativo')
elif numero % 2 != 0 and numero > 0:
    print(f'O número {numero} é impar e positivo')
elif numero % 2 != 0 and numero < 0:
    print(f'O número {numero} é impar e negativo')
else:
    print(f'O número {numero}')