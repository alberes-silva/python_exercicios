while True:
    multiplo = []
    numero = int(input("Digite um valor: "))
    valorMaximo = int(input("Digite o valor máximo: "))
    for i in range(numero, valorMaximo + 1):
        if i % numero == 0:  
            multiplo.append(i)  
    
    print(f"Os múltiplos de {numero} até {valorMaximo} são: {multiplo}")