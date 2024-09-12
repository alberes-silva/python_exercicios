salario = float(input("Informe o seu salário R$ "))

if 0 < salario <= 2500:
    aumento = salario * 1.07
    print(f'Seu salário R$ {salario}, na faixa baixa, aumento de 7%, salário final R$ {aumento}')
elif 2501 < salario <= 5000:
    aumento = salario * 1.05
    print(f'Seu salário R$ {salario}, na faixa média, aumento de 5%, salário final R$ {aumento}')
else:
    aumento = salario * 1.03
    print(f'Seu salário R$ {salario}, na faixa alta, aumento de 3%, salário final R$ {aumento}')