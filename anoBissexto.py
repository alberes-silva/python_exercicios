ano = int(input('Informe o ano desejado: '))

if ano % 4 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')