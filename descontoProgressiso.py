
produto1 = float(input('Informe o valor da produto: '))
produto2 = float(input('Informe o valor da produto: '))
produto3 = float(input('Informe o valor da produto: '))
resultadoTotal = produto1+produto2+produto3

if resultadoTotal >= 500 and resultadoTotal <1000:
    desconto = resultadoTotal*0.10
    valorFinal = resultadoTotal - desconto
    print(f'O valor inicial é R${resultadoTotal}, com desconto de 15% R${desconto}, valor final R${valorFinal}')
else:
    desconto = resultadoTotal*0.15
    valorFinal = resultadoTotal - desconto
    print(f'O valor inicial é R${resultadoTotal}, com desconto de 15% R${desconto},valor final R${valorFinal}')

