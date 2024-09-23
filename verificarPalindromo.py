palavra = input('Digite a sua palavra ou frase: ')

palavra_minusscula = palavra.replace(" ", "").lower()

palindromo = True

# Usar um loop for para verificar se a palavra é um palíndromo
for i in range(len(palavra_minusscula) // 2):
    if palavra_minusscula[i] != palavra_minusscula[-(i + 1)]:
        palindromo = False
        break 


if palindromo:
    print(f'A palavra "{palavra}" é um Palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um Palíndromo.')

