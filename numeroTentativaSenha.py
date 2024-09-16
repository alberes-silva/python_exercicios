import random
import math

senha = math.ceil(10 * random.random())

tentativa = 3
contador = 1

while tentativa >= contador:
    acesso = int(input('Digite a senha correta: (dica: 0 a 10) '))
    if acesso == senha:
        print("Você digitou a senha correta!")
        break
    else:
        print("Senha incorreta, tente novamente!")
    contador += 1
